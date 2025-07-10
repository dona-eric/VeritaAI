import streamlit as st

st.markdown("""
    <style>
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

        /* Liste d'aide */
        .help-list {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.05em;
            color: #444444;
            list-style-type: disc; /* Puces par défaut */
            padding-left: 25px; /* Indentation des puces */
        }
        .help-list li {
            margin-bottom: 10px;
        }
        .help-list strong {
            color: #3f51b5; /* Couleur d'accent pour les titres de section */
        }
        .contact-info {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.1em;
            color: #333333;
            margin-top: 30px;
            text-align: center;
        }
        .contact-info a {
            color: #3f51b5;
            text-decoration: none;
            font-weight: bold;
        }
        .contact-info a:hover {
            text-decoration: underline;
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
def help_page():
    st.markdown("<h1 class='section-title'>📘 Centre d'aide Verita</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Retrouvez ici les informations essentielles pour tirer le meilleur parti de votre application Verita.</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<h3><strong>Comment utiliser VeritaAI ?</strong></h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul class="help-list">
        <li><strong>Étape 1 : Accédez à la section "Analyse".</strong>
            <ul><li>Cliquez sur le bouton "Lancer l'analyseur" depuis la page d'accueil.</li></ul>
        </li>
        <li><strong>Étape 2 : Saisissez l'information à analyser.</strong>
            <ul><li>Collez le texte de l'article, du post de réseau social, ou toute autre information que vous souhaitez vérifier dans la zone de texte prévue à cet effet.</li></ul>
        </li>
        <li><strong>Étape 3 : Lancez l'analyse.</strong>
            <ul><li>Cliquez sur le bouton "Analyser l'information" et attendez quelques instants. Notre intelligence artificielle traitera le contenu.</li></ul>
        </li>
        <li><strong>Étape 4 : Obtenez le "Verdict".</strong>
            <ul><li>Verita vous affichera une "Prédiction" indiquant si l'information est jugée probable "VRAIE" ou "FAUSSE", accompagnée de brèves explications.</li></ul>
        </li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<h3><strong>Conseils pour une meilleure utilisation :</strong></h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul class="help-list">
        <li><strong>Texte Clair et Complet :</strong> Pour des analyses plus précises, essayez de fournir un texte aussi clair et complet que possible.</li>
        <li><strong>Esprit Critique :</strong> Verita est un outil d'aide. Continuez toujours de croiser les sources et de développer votre esprit critique.</li>
    </ul>
    """, unsafe_allow_html=True)


    st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
    st.markdown("<h3><strong>Besoin d'aide supplémentaire ?</strong></h3>", unsafe_allow_html=True)
    st.markdown("Si vous avez des questions, des suggestions, ou rencontrez des problèmes, n'hésitez pas à nous contacter :")
    st.markdown("Support:<a href='mailto:donaerickoulodji@gmil.com'>donaerickoulodji@gmail.com</a>")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Retour à l'Accueil", key="back_to_home_help"): # Clé unique
        st.session_state.page = "home"
        st.rerun()

if __name__ == "__main__":
    help_page()