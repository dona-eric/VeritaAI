import streamlit as st
st.set_page_config(
    page_title="VeritaAI - Détection des Fake News",
    page_icon="🧠",
    layout="wide"
)
from pages.login import login_page
from pages.analyse import analyse_page
from pages.help import help_page
from pages.home import home_page



# ----- STYLE CSS PERSONNALISÉ -----
# --- Style CSS Professionnel & Élégant avec Dégradé de Gris ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:wght@400;700&display=swap');

    /* Styles généraux pour le corps et les éléments Streamlit */
    html, body {
        /* Dégradé de gris élégant */
        background: linear-gradient(135deg, #e0e0e0 0%, #f0f0f0 100%);
        font-family: 'Montserrat', serif; /* Police moderne et lisible */
        color: #333333; /* Texte gris foncé pour la lisibilité */
        line-height: 1.6;
    }
    .main {
        background: none; /* Permet au dégradé du body de transparaître */
        padding: 20px; /* Ajoute un peu de padding au contenu principal */
    }
    .css-h5rpku { /* Sélecteur spécifique pour le conteneur principal du contenu Streamlit */
        background-color: rgba(255, 255, 255, 0.9); /* Fond blanc semi-transparent pour les sections de contenu */
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08); /* Ombre douce et professionnelle */
        padding: 30px;
        margin-top: 30px;
    }

    /* Conteneur de l'en-tête (Logo et Titres) */
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 40px 0;
        background-color: rgba(255, 255, 255, 0.95); /* Fond blanc presque opaque pour l'en-tête */
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); /* Ombre plus prononcée pour l'élément clé */
        margin-bottom: 50px;
        animation: fadeInScale 1.5s ease-out forwards; /* Animation d'apparition */
    }

    /* Style du logo */
    .logo-img {
        max-width: 80px; /* Taille adéquate */
        height: 50px;
        border-radius: 0%; /* Rendre le logo rond */
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1); /* Ombre légère autour du logo */
        margin-bottom: 25px;
        transition: transform 0.3s ease-in-out;
    }
    .logo-img:hover {
        transform: scale(1.05); /* Effet au survol */
    }

    /* Titre principal de l'application */
    .title {
        font-family: 'Playfair Display', serif; /* Police élégante pour le titre */
        font-size: 3.8em;
        font-weight: 700;
        color: #3f51b5; /* Un bleu plus profond et élégant (Material Design Blue 500) */
        margin-bottom: 10px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.08); /* Ombre subtile */
        animation: slideInFromTop 1.5s ease-out forwards;
    }

    /* Sous-titres */
    .subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.5em;
        color: #555555;
        max-width: 700px;
        line-height: 1.7;
        margin-bottom: 15px;
        animation: fadeIn 2s ease-in forwards;
    }
    .subtitle-agent { /* Utilisé pour des messages ou des slogans clés */
        font-family: 'Montserrat', sans-serif;
        font-size: 1.3em;
        font-weight: 600;
        color: #4a6a7a; /* Un gris-bleu harmonieux */
        margin-bottom: 20px;
        animation: fadeIn 2.5s ease-in forwards;
    }

    /* Titres de section pour le contenu */
    .section-title {
        font-family: 'Playfair Display', serif;
        color: #2c3e50; /* Bleu très foncé, presque noir */
        font-size: 2.5em;
        font-weight: 700;
        margin-top: 50px;
        margin-bottom: 25px;
        text-align: center;
        position: relative; /* Pour le pseudo-élément */
    }
    .section-title::after {
        content: '';
        display: block;
        width: 80px; /* Longueur de la ligne */
        height: 4px; /* Épaisseur de la ligne */
        background-color: #3f51b5; /* Couleur de la ligne */
        margin: 10px auto 0; /* Centre la ligne sous le titre */
        border-radius: 2px;
        animation: expandLine 1.5s ease-out forwards;
    }

    /* Paragraphes de contenu */
    p {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.05em;
        line-height: 1.7;
        color: #444444;
        text-align: justify;
        margin-bottom: 15px;
    }

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
def main():
    # initialisation des roles de connexion
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "role" not in st.session_state:
        st.session_state.role = "user"
    if "role_selected" not in st.session_state:
        st.session_state.role_selected = False
    if "email_verified" not in st.session_state:
        st.session_state.email_verified = False


    # Sélection du rôle utilisateur
    if "role_selected" not in st.session_state:
        role = st.selectbox("Sélectionnez votre rôle :", ["User", "Admin", "Super-Admin"])
        if st.button("Confirmed", type="primary"):
            st.session_state.role = role
            st.session_state.role_selected = True
            st.rerun()
        return
    if st.session_state.role == "user":
            if not st.session_state.authenticated:
                login_page()
                return
            else:
                show_navigation_menu()

    elif st.session_state.role in ["admin", "super-admin"]:
        if not st.session_state.email_verified:
            # Vérification email pour admin/super-admin
            verify_admin_email()
            return
        else:
            # Admin vérifié - Accès direct au menu
            show_navigation_menu()

def verify_admin_email():
    """Vérification email pour admin/super-admin"""
    st.title(f"Vérification - {st.session_state.role.title()}")
    st.write("Veuillez vérifier votre email pour accéder aux fonctionnalités d'administration.")
    
    email = st.text_input("Email", placeholder="admin@exemple.com", label="Entrer votre email")
    
    if st.button("Verification State", type="primary"):
        if email and "@" in email:  # Validation basique
            st.session_state.email_verified = True
            st.session_state.admin_email = email
            st.success(f"Email vérifié ! Bienvenue {st.session_state.role}.")
            st.rerun()
        else:
            st.error("Veuillez saisir un email valide")

def show_navigation_menu():

    """Affiche le menu de navigation pour les utilisateurs authentifiés"""
    if st.session_state.role == "user":
    # Informations utilisateur dans la sidebar
        st.sidebar.title("🗂️ Navigation")
    #st.sidebar.info(f"**Rôle :** {st.session_state.role.title()}")
    
    #if st.session_state.role == "user":
        #st.sidebar.success("✅ Connecté en tant qu'utilisateur")
    #else:
        #st.sidebar.success(f"✅ Email vérifié")
    
    # Bouton de déconnexion
    if st.sidebar.button("🚪 Déconnexion"):
        # Reset complet de la session
        st.session_state.authenticated = False
        st.session_state.role_selected = False
        st.session_state.email_verified = False
        st.session_state.role = "user"
        st.rerun()
    
    # Menu de navigation
    menu_options = ["Home", "Analyse", "Help"]
    menu = st.sidebar.selectbox("", menu_options)
    
    # Routage vers les pages
    if menu == "Home":
        home_page()
    elif menu == "Analyse":
        analyse_page()
    elif menu == "Help":
        help_page()

if __name__=="__main__":
    main()