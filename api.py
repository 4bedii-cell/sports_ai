from fastapi import FastAPI
import numpy as np
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Sports AI en ligne 🚀"}

# Foot - modèle Poisson simplifié
@app.get("/predict/foot")
def predict_foot(home: str = "PSG", away: str = "Marseille"):
    lam_home = np.random.uniform(1, 2.5)
    lam_away = np.random.uniform(0.5, 2)
    return {
        "match": f"{home} vs {away}",
        "expected_goals": {"home": round(lam_home, 2), "away": round(lam_away, 2)},
        "prediction": "Home Win" if lam_home > lam_away else "Away/Draw"
    }

# NBA - moyenne glissante simplifiée
@app.get("/predict/nba")
def predict_nba(player: str = "LeBron James"):
    last5 = [random.randint(18, 35) for _ in range(5)]
    avg = np.mean(last5)
    return {
        "player": player,
        "last5_games": last5,
        "projected_points": round(avg + np.random.uniform(-2, 2), 1)
    }
