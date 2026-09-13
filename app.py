import streamlit as st

st.set_page_config(page_title="Mes cours de maths", page_icon="📚")

st.title("📚 Mes cours de mathématiques")

# --- Config : un dictionnaire thème -> chapitres -> URL ---
BASE_URL = "https://ton-pseudo.github.io/nom-du-repo"

CHAPITRES = {
    "Second degré": {
        "url": f"{https://github.com/maelmoignet-pixel/cours-premieres/blob/main}/second-degre.html",
        "icone": "📐",
        "description": "Fonctions polynômes, forme canonique, équations, signe du trinôme."
    },
    # Ajoute tes futurs chapitres ici, par exemple :
    # "Suites numériques": {
    #     "url": f"{BASE_URL}/suites.html",
    #     "icone": "🔢",
    #     "description": "Récurrence, limites, opérations."
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
