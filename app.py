import streamlit as st
import requests

st.set_page_config(page_title="Sports AI", page_icon="⚽🏀")

st.title("📊 Sports AI Predictions")

choice = st.sidebar.selectbox("Choisis ton sport", ["Football", "NBA"])

if choice == "Football":
    home = st.text_input("Équipe domicile", "PSG")
    away = st.text_input("Équipe extérieur", "Marseille")
    if st.button("Prédire"):
        res = requests.get("https://TON-BACKEND-RENDER.onrender.com/predict/foot", params={"home": home, "away": away}).json()
        st.json(res)

if choice == "NBA":
    player = st.text_input("Nom du joueur", "LeBron James")
    if st.button("Prédire"):
        res = requests.get("https://TON-BACKEND-RENDER.onrender.com/predict/nba", params={"player": player}).json()
        st.json(res)
