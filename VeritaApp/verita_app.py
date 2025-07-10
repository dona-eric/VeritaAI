import streamlit as st
import joblib,logging, os
import numpy as np
from PIL import Image
from datetime import datetime
# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === Chemins de base ===
MODEL_DIR = "../models_save"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")


# ----- CONFIGURATION -----
st.set_page_config(
    page_title="VeritaAI - Détection d'actualités fiables",
    page_icon="🛡️📢",
    layout="centered"
)

try:
    # ----- CHARGEMENT DU LOGO -----
    logo_path = "../Fake_News/VeritaApp/assets/veritaAI.png"
    logo = Image.open(logo_path)
except FileNotFoundError:
    logo = None

# ----- STYLE CSS PERSONNALISÉ -----
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
        body {
            background: linear-gradient(145deg, #8c998c1c, #d0e6e2bb);
            color: #d0e6e2bb;
            font-family: Liberation Serif Italic;
        }
        .title {
            font-size: 150px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
            color: #50a8ff;
            animation: slideIn 2s ease-out forwards;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #d0e6e2bb;
            margin-bottom: 10px;
            transform: 0.3s ease;
            animation: fadeIn 3s ease-in;

        }
        .subtitle-agent {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            color: #d0e6e2bb;
            margin-bottom: 10px;
            transform: 0.3s ease;
            animation: fadeIn 3s ease-in;
        }
        .footer {
            font-size: 12px;
            text-align: center;
            color: gray;
            margin-top: 40px;
        }
        .stButton > button {
            background-color: #50a8ff;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            padding: 0.5em 1.2em;
            margin-top: 1em;
            transition: 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #2e86c1;
            transform: scale(1.03);
        }
        @keyframes fadeIn {
            from { opacity: 0;}
            to { opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

def main():
    # ----- CONTENU -----
    if logo:

        st.markdown('<div class="title">VeritaAI</div>', unsafe_allow_html=True)
        st.image(logo, use_container_width=True, width=150)
        st.markdown("<div class='subtitle'>🛡️ VeritaAI, Qu'est ce que c'est ? C'est une plateforme mais pas n'importe laquelle." \
        " La propagation rapide des fausses nouvelles sur les réseaux sociaux 🖍️🖍️ et " \
        "les plateformes en ligne constitue une menace majeure pour la société moderne." \
        "Ces informations trompeuses peuvent manipuler l'opinion publique, influencer des élections ou encore alimenter des tensions sociales. " \
        " 📵📵 Dans ce contexte numérique à l'ère actuelle, il devient crucial de développer des systèmes intelligents capables de détecter automatiquement ces fausses informations.</div>",
                    unsafe_allow_html=True)
        
        st.markdown("<div class='subtitle-agent'>🏆 Je vous présente votre meilleure plateforme de détection, " \
        "vérification des vraies informations. " \
        "  Votre assistant intelligent pour distinguer le vrai du faux dans l'actualité."
        "</div>", unsafe_allow_html=True)

        st.write("---")

        st.write("### 🔍 Fonctionnalités principales")
        st.markdown("""
        - **Analyse automatique des titres, contenus et descriptions d’articles.**
        - **Détection en temps réel de fausses informations à partir des vraies informations sur les sites.**
        - **Intuitive et accessible via le web .**
        - **Données stockées et exportables en CSV.**
        """)

        st.write("### 🚀 **Prêt à commencer ?**")
        st.success("Allez dans le menu à gauche pour analyser vos contenus d’actualité.")

    if st.button("Analyse 📈"):
        st.spinner("🔗 Rediriger vers la page d'analyse...")

    #st.write("---")

    st.markdown(f'<div class="footer">© {datetime.now().year} VeritaAI-Propulsé par Streamlit</div>',
                unsafe_allow_html=True)


if __name__ == "__main__":
    main()
