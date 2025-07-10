import streamlit as st
import time
from pages.home import home_page
def analyse_page():
    st.markdown("""
        <style>
            .stButton > button {
                background-color: #50a8ff;
                color: white;
                font-weight: bold;
                border-radius: 6px;
                padding: 0.5em 1em;
                transition: 0.3s ease-in-out;
            }
            .stButton > button:hover {
                background-color: #2e86c1;
                transform: scale(1.02);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='section-title'>🔎 Détecteur des Vraies Informations</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Bienvenue sur la page de détection ! Ici, vous pourrez soumettre le texte que vous souhaitez analyser.</p>", unsafe_allow_html=True)

    texte = st.text_area(
        label="📝 Texte d'actualité",
        placeholder="Copiez-collez ici le contenu ou le titre d'une actualité...",
        height=300
    )

    if st.button("Analyser"):
        if texte.strip():
            with st.spinner("Analyse en cours... Veuillez patienter."):
                time.sleep(3)
            st.success("Analyse terminée ! Voici le résultat :")
            st.markdown("---")
            st.subheader("Verdict de Verita :")
                # Simulation d'un résultat
                
        else:
            st.warning("Veuillez entrer du texte pour l'analyse.")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Retour à l'Accueil", key="back_to_home"):
        st.rerun()
        home_page()
        st.stop()
if __name__ == "__main__":
    analyse_page()
