import streamlit as st
import os
from datetime import datetime
from PIL import Image


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:wght@400;700&display=swap');

    /* Styles généraux pour le corps et les éléments Streamlit */
    html, body, .stApp {
        /* Dégradé de gris élégant */
        background: linear-gradient(135deg, #f9f9f6 0%, #dbe9f4 100%);
        font-family: 'Montserrat', sans-serif; /* Police moderne et lisible */
        color: #333330; /* Texte gris foncé pour la lisibilité */
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
        max-width: 180px; /* Taille adéquate */
        height: auto;
        border-radius: 50%; /* Rendre le logo rond */
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
        font-size: 1.2em;
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
    </style>
""", unsafe_allow_html=True)


def home_page():
    st.markdown("<div class='header-container'>", unsafe_allow_html=True)

    try:
        # ----- CHARGEMENT DU LOGO -----
        logo_path = "../Fake_News/VeritaApp/assets/veritaAI.png"
        logo = Image.open(logo_path)
        st.image(logo, use_container_width=True, width=200, clamp=False,
                channels="BGR",output_format="PNG", caption="")
    except FileNotFoundError:
        logo = None
    
    st.markdown("<h1 class='title'>Verita</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>🛡️ VeritaAI, Qu'est ce que c'est ? C'est une plateforme mais pas n'importe laquelle." \
        " La propagation rapide des fausses nouvelles sur les réseaux sociaux 🖍️🖍️ et " \
        "les plateformes en ligne constitue une menace majeure pour la société moderne." \
        "Ces informations trompeuses peuvent manipuler l'opinion publique, influencer des élections ou encore alimenter des tensions sociales. " \
        " 📵📵 Dans ce contexte numérique à l'ère actuelle, il devient crucial de développer des systèmes intelligents capables de détecter automatiquement ces fausses informations.</div>",
                    unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

        
    st.markdown("<div class='subtitle-agent'>🏆 Je vous présente votre meilleure plateforme de détection, " \
        "vérification des vraies informations. " \
        "  Votre assistant intelligent pour distinguer le vrai du faux dans l'actualité."
        "</div>", unsafe_allow_html=True)

    st.write("---")

    st.markdown("<p class='section-title'>Pourquoi utiliser Verita ?</p>", unsafe_allow_html=True)
    st.write("""
        1.  **Saisissez ou collez votre information :** Qu'il s'agisse d'un article, d'un post de réseau social ou d'un simple texte.
        2.  **Analysez :** Notre IA examine le contenu, la source, le style et d'autres paramètres clés.
        3.  **Obtenez un verdict :** Recevez une évaluation de la fiabilité de l'information.
        """)

    st.markdown("<p class='section-title'>Prêt à commencer ?</p>", unsafe_allow_html=True)
    st.write("Cliquez sur le bouton ci-dessous pour lancer l'analyse d'une information.")


    if st.button("Analyse 📈"):
        st.session_state["menu"] = "analyse"
        st.rerun()
    #st.write("---")

    st.markdown(f'<div class="footer"> © {datetime.now().year} VeritaAI- Tous droit réservés</div>',
                unsafe_allow_html=True)


if __name__ == "__main__":
    home_page()
