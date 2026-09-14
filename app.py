import streamlit as st

st.set_page_config(page_title="Mes cours de maths", page_icon="📚")

# --- Config : URL de base de ton site GitHub Pages (racine du dépôt) ---
BASE_URL = "https://maelmoignet-pixel.github.io/cours-premieres"

# --- En-tête avec titre + signature ---
st.markdown(
    """
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <h1 style="margin-bottom: 0;">📚 Mes cours de mathématiques</h1>
        <p style="font-size: 18px; color: #4a4a4a; margin-top: 5px;">
            par <strong>Maël Moignet</strong>
        </p>
        <p style="font-size: 15px; color: #7a7a7a; margin-top: -8px;">
            🎓 Lycée Naval de Brest
        </p>
    </div>
    <hr style="margin-bottom: 25px;">
    """,
    unsafe_allow_html=True
)

# Un dictionnaire : nom du chapitre -> infos (url, icône, description)
# Chaque chapitre vit dans son propre dossier : <nom-dossier>/<fichier>.html
CHAPITRES = {
    "Second degré": {
        "url": f"{BASE_URL}/second-degre/second-degre.html",
        "icone": "📐",
        "description": "Fonctions polynômes, forme canonique, équations, signe du trinôme."
    },
    "Suites numériques": {
        "url": f"{BASE_URL}/suites/suites.html",
        "icone": "🔢",
        "description": "Modes de génération, sens de variation, limites."
    },
}

st.subheader("Choisis un chapitre :")

for nom, infos in CHAPITRES.items():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"### {infos['icone']} {nom}")
        st.write(infos["description"])
    with col2:
        st.link_button("Ouvrir ➜", infos["url"], use_container_width=True)
    st.write("---")

# --- Pied de page ---
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; color: #999; font-size: 13px;">
        Site réalisé par Maël Moignet — Lycée Naval de Brest
    </div>
    """,
    unsafe_allow_html=True
)
