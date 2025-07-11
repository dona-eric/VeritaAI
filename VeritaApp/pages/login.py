import streamlit as st
from pages.home import home_page


st.markdown("""

    <style>
            /* Boutons */
    .stButton > button {
        background-color: #3f51b5; /* Bleu Material Design */
        color: white;
        font-weight: 600; /* Moins gras que bold */
        border: none;
        border-radius: 10px; /* Coins arrondis */
        padding: 0.9em 2.5em; /* Plus de padding */
        margin-top: 2em; /* Plus d'espace au-dessus */
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15); /* Ombre plus visible */
    }
    .stButton > button:hover {
        background-color: #303f9f; /* Bleu plus foncé au survol */
        transform: translateY(-5px) scale(1.02); /* Léger mouvement vers le haut et agrandissement */
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25); /* Ombre plus intense au survol */
    }
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    /* Pied de page */
    .footer {
        font-family: 'Montserrat', sans-serif;
        font-size: 0.85em;
        text-align: center;
        color: #777777;
        margin-top: 70px;
        padding: 25px 0;
        border-top: 1px solid #e5e5e5;
    }

    /* Styles pour les messages d'info/succès/erreur (améliorés) */
    .stAlert {
        border-radius: 10px;
        padding: 20px;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.05em;
        margin-top: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    .stAlert.info { border-left: 6px solid #2196f3; background-color: #e3f2fd; color: #1e88e5; } /* Bleu clair */
    .stAlert.success { border-left: 6px solid #4caf50; background-color: #e8f5e9; color: #388e3c; } /* Vert clair */
    .stAlert.warning { border-left: 6px solid #ff9800; background-color: #fff3e0; color: #fb8c00; } /* Orange clair */
    .stAlert.error { border-left: 6px solid #f44336; background-color: #ffebee; color: #d32f2f; } /* Rouge clair */


    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInScale {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
    }
    @keyframes slideInFromTop {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes expandLine {
        from { width: 0; }
        to { width: 80px; }
    }

    /* Optimisation pour les zones de texte et autres entrées */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 10px 15px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.08);
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #3f51b5;
        box-shadow: 0 0 0 3px rgba(63, 81, 181, 0.2); /* Halo de focus élégant */
        outline: none;
    }
    </style>
""", unsafe_allow_html=True)

def login_page():
    st.header("🔐 Créer un compte VeritaAI")
    st.markdown("Connectez-vous avec VeritaAI")

    nom = st.text_input("Nom", help="Entrez votre nom")
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        # Exemple : Identifiants fictifs de test
        if email == "test@verita.ai" and password == "verita123":
            st.success("Connecté avec succès !")
            st.session_state.authenticated = True
            st.session_state.user_name=nom
            st.session_state.email = email
            st.session_state.redirect_page = "Home"
            st.rerun()
    
        else:
            st.error("Identifiants incorrects.")
            st.rerun()
if __name__ == "__main__":
    login_page()