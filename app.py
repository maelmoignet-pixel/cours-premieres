import streamlit as st

st.set_page_config(page_title="Mes cours de maths", page_icon="📚")

st.title("📚 Mes cours de mathématiques")

# --- Config : URL de base de ton site GitHub Pages (racine du dépôt) ---
BASE_URL = "https://maelmoignet-pixel.github.io/cours-premieres"

# Un dictionnaire : nom du chapitre -> infos (url, icône, description)
# Chaque chapitre vit dans son propre dossier : <nom-dossier>/<fichier>.html
CHAPITRES = {
    "Second degré": {
        "url": f"{BASE_URL}/second-degre/second-degre.html",
        "icone": "📐",
        "description": "Fonctions polynômes, forme canonique, équations, signe du trinôme."
    },
    # Ajoute tes futurs chapitres ici, en suivant le même modèle :
    # "Suites numériques": {
    #     "url": f"{BASE_URL}/suites/suites.html",
    #     "icone": "🔢",
    #     "description": "Modes de génération, sens de variation, limites."
    # },
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
