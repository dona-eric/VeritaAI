import streamlit as st
import requests, mlflow, mlflow.sklearn, joblib



st.title("Systèmes de détection de fausses nouvelles")
# Load the model from the MLflow model registry
def load_model():
    try:
        model_path="/home/dona-erick/Fake_News/Analyse/mlartifacts/0/models/m-0a82c951527448bd9715906f461f7cb0/artifacts/model.pkl"
        model = mlflow.sklearn.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {e}")
        return None
    
def load_vectorizer():
    try:
        vectorizer = joblib.load('../models_save/vectorizer.pkl')
        return vectorizer
    except Exception as e:
        st.error(f"Erreur lors du chargement du vectorizer : {e}")
        return None
    

if st.button('Prédiction'):
    vectorizer = load_vectorizer()
    model = load_model()
    if model and vectorizer:
        user = st.text_area("Entrez le texte à analyser pour les fake news :")
        if user:
            # Vectoriser le texte d'entrée
            text_vectorized = vectorizer.transform([user])
            # Faire la prédiction
            prediction = model.predict(text_vectorized)
            prediction_proba = model.predict_proba(text_vectorized)
            st.write(f"Prédiction : {'Fake News' if prediction[0] == -1 else 'Real News'}")
            st.write(f"Probabilités : {prediction_proba}")
    else:
        st.error("Le modèle ou le vectorizer n'a pas pu être chargé.")