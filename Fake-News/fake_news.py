import streamlit as st
import joblib
import logging
import os
import numpy as np

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === Chemins de base ===
MODEL_DIR = "../models_save"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")


# === Fonctions utilitaires ===
@st.cache_resource
def load_model(path=MODEL_PATH):
    try:
        model = joblib.load(path)
        logger.info("Modèle chargé avec succès.")
        return model
    except Exception as e:
        logger.error(f"Erreur lors du chargement du modèle : {e}")
        st.error(f"Erreur lors du chargement du modèle : {e}")
        return None

@st.cache_resource
def load_vectorizer(path=VECTORIZER_PATH):
    try:
        vectorizer = joblib.load(path)
        logger.info("Vectorizer chargé avec succès.")
        return vectorizer
    except Exception as e:
        logger.error(f"Erreur lors du chargement du vectorizer : {e}")
        st.error(f"Erreur lors du chargement du vectorizer : {e}")
        return None

def predict_news(text, model, vectorizer):
    try:
        vectorized_text = vectorizer.transform([text])
        prediction = model.predict(vectorized_text)[0]
        prediction_proba = None
        if hasattr(model, "predict_proba"):
            prediction_proba = model.predict_proba(vectorized_text)[0]
        return prediction, prediction_proba
    except Exception as e:
        logger.error(f"Erreur lors de la prédiction : {e}")
        st.error(f"Erreur lors de la prédiction : {e}")
        return None, None


# === Interface utilisateur ===
def main():
    st.title("📰 Système de Détection de Fausses Nouvelles")
    st.markdown("Entrez un texte d’actualité pour prédire s’il s’agit d’une fake news ou non.")

    text_input = st.text_area("🖊️ Entrez le texte à analyser :", height=200)

    if st.button("🔍 Lancer la prédiction"):

        model = load_model()
        vectorizer = load_vectorizer()

        if not model or not vectorizer:
            st.warning("Le modèle ou le vectorizer est introuvable.")
            return

        if text_input.strip() == "":
            st.warning("Veuillez entrer un texte.")
            return

        prediction, prediction_proba = predict_news(text_input, model, vectorizer)

        if prediction is not None:
            label = "🟥 Fake News" if prediction == -1 else "🟩 Real News"
            st.subheader(f"Résultat : {label}")
            if prediction_proba is not None:
                st.write("Probabilités (classes) :", np.round(prediction_proba, 3))
        else:
            st.error("Erreur dans la prédiction.")

if __name__ == "__main__":
    main()
