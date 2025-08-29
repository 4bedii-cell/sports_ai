import streamlit as st
import requests

st.set_page_config(page_title="Sports AI", page_icon="⚽🏀")
st.title("📊 Sports AI Predictions")

# URL publique du backend Render
BACKEND_URL = "https://TON-BACKEND-RENDER.onrender.com"

choice = st.sidebar.selectbox("Choisis ton sport", ["Football", "NBA"])

if choice == "Football":
    home = st.text_input("Équipe domicile", "PSG")
    away = st.text_input("Équipe extérieur", "Marseille")
    if st.button("Prédire"):
        try:
            res = requests.get(f"{BACKEND_URL}/predict/foot", params={"home": home, "away": away}).json()
            st.json(res)
        except Exception as e:
            st.error(f"Erreur de connexion au backend : {e}")

if choice == "NBA":
    player = st.text_input("Nom du joueur", "LeBron James")
    if st.button("Prédire"):
        try:
            res = requests.get(f"{BACKEND_URL}/predict/nba", params={"player": player}).json()
            st.json(res)
        except Exception as e:
            st.error(f"Erreur de connexion au backend : {e}")
