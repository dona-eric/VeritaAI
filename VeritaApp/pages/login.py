import streamlit as st
from pages.home import home_page
def login_page():
    st.header("🔐 Créer un compte VeritaAI")
    st.markdown("Connectez-vous avec VeritaAI")

    nom = st.text_input("Nom", help="Entrez votre nom")
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        # Exemple : Identifiants fictifs de test
        if email == "test@verita.ai" and password == "verita123":
            st.success("✅ Connecté avec succès !")
            st.session_state.authenticated = True
            home_page()
        else:
            st.error("Identifiants incorrects.")
            st.rerun()
if __name__ == "__main__":
    login_page()