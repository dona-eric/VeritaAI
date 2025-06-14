import pandas as pd
import numpy as np
import warnings, sys, os, re, joblib
import nltk, mlflow, mlflow.sklearn
mlflow.set_tracking_uri("http://127.0.0.1:5000")
from mlflow.models import infer_signature
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from nltk.stem import WordNetLemmatizer, PorterStemmer, SnowballStemmer, LancasterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.utils import resample

## télechargement des données
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
warnings.filterwarnings("ignore")

## charger les données
def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")
    return pd.read_csv(file_path)


# Prétraitement des données
def preprocess_text(text):
    if pd.isnull(text):
        return ""
    text = str(text)
    # Tokenisation
    tokens = nltk.word_tokenize(text)
    # Lemmatisation
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Fonction pour vectoriser le texte
def vectorize_text(X_train, X_test, vectorizer_type='tfidf'):
    if vectorizer_type == 'tfidf':
        vectorizer = TfidfVectorizer(stop_words='english')
    elif vectorizer_type == 'count':
        vectorizer = CountVectorizer(stop_words='english')
    else:
        raise ValueError("vectorizer_type doit être 'tfidf' ou 'count'")
    
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    joblib.dump(vectorizer, 'vectorizer.pkl')  # Sauvegarder le vectorizer pour une utilisation future
    print(f"Vectorisation terminée avec le type de vectoriseur : {vectorizer_type}")
    return X_train_vectorized, X_test_vectorized, vectorizer

# Fonction pour entraîner le modèle
def train_model(X_train, y_train):
    models = [
        ('Naive Bayes', MultinomialNB()),
        ('Logistic Regression', LogisticRegression()),
        ('Linear SVM', LinearSVC()),
        ('SVM', SVC()),
    ]

    for name, model in models:
        model.fit(X_train, y_train)
        print(f"{name} entraîné avec succès.")
        yield name, model

# Fonction pour évaluer le modèle
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Rapport de classification :\n", classification_report(y_test, y_pred))
    print("Matrice de confusion :\n", confusion_matrix(y_test, y_pred))
    print("Précision :", accuracy_score(y_test, y_pred))
    print("F1 Score :", f1_score(y_test, y_pred, average='weighted'))
    print("Précision :", precision_score(y_test, y_pred, average='weighted'))
    print("Rappel :", recall_score(y_test, y_pred, average='weighted'))


# Fonction principale pour l'analyse des fake news
def analyze_fake_news(file_path, vectorizer_type='tfidf'):
    # Charger les données
    df = load_data(file_path)
    # Vérifier les colonnes attendues
    if 'cleaned_text' not in df.columns or 'label' not in df.columns:
        raise ValueError("Le fichier doit contenir les colonnes 'text' et 'label'.")
    # Prétraiter le texte
    df['text_initial'] = df['cleaned_text'].apply(preprocess_text)
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(df['text_initial'], df['label'], test_size=0.2, random_state=42)
    # Vectoriser le texte
    X_train_vectorized, X_test_vectorized, vectorizer = vectorize_text(X_train, X_test, vectorizer_type)
    
    # Entraîner et évaluer les modèles
    for name, model in train_model(X_train_vectorized, y_train):
        with mlflow.start_run(run_name=name):
            mlflow.log_param("model_type", name)
            mlflow.sklearn.log_model(model, "model")
            mlflow.log_param("vectorizer_type", vectorizer_type)
            print(f"Évaluation du modèle {name} :")
            evaluate_model(model, X_test_vectorized, y_test)
            print("\n" + "="*50 + "\n")
            y_pred = model.predict(X_test_vectorized)
            mlflow.log_metric("f1_score", f1_score(y_test, y_pred, average='weighted'))
            mlflow.log_metric("precision", precision_score(y_test, y_pred, average='weighted'))
            mlflow.log_metric("recall", recall_score(y_test, y_pred, average='weighted'))
            mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
            mlflow.sklearn.log_model(model, 
                                     name="model",
                                     input_example=X_test_vectorized[:1],
                                     signature = infer_signature(X_test_vectorized, y_pred))

file_path ="/home/dona-erick/Fake_News/data_cleaned/cleaned_news_dataset.csv"
analyze_fake_news(file_path, vectorizer_type='tfidf')