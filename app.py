import streamlit as st
import streamlit.components.v1 as components

with open("second-degre.html", "r", encoding="utf-8") as f:
    html_content = f.read()


st.set_page_config(page_title="Mes cours de maths", page_icon="📚")

st.title("📚 Mes cours de mathématiques")

# --- Config : un dictionnaire thème -> chapitres -> URL ---
BASE_URL = "https://maelmoignet-pixel.github.io/cours-premieres"

CHAPITRES = {
    "Second degré": {
        "url": f"{BASE_URL}/second-degre.html",
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
