import streamlit as st
import pandas as pd
import joblib

# Chargement des données et du modèle
df_total = pd.read_csv("df_total.csv", index_col=0)
X_test_imp = pd.read_csv("X_test_imp.csv", index_col=0)
xgb_model = joblib.load("xgb_model.pkl")
le = joblib.load("label_encoder.pkl")

st.title("Prédiction Résultat Match L1")

# Choix du match
match_index = st.slider("Choisissez un match à prédire avec le curseur ci-dessous", 0, len(X_test_imp) - 1, 0)
match_features = X_test_imp.iloc[[match_index]]
match_id = X_test_imp.index[match_index]

# Infos match (par position)
infos_match = df_total.iloc[match_index][["Match_Date", "Home_Team", "Away_Team", "Saison"]]
st.subheader("📋 Détails du match")
st.write(f" **Date :** {infos_match['Match_Date']}")
st.write(f" **Domicile :** {infos_match['Home_Team']}")
st.write(f" **Extérieur :** {infos_match['Away_Team']}")
st.write(f" **Saison :** {infos_match['Saison']}")

# Saisie de la cote proposée par le bookmaker
bookmaker_odd = st.number_input("=> Entrez la cote proposée par le bookmaker pour l'issue prédite", min_value=1.01, step=0.01)

# Prédiction
if st.button("✨-Prédire-✨"):
    pred_encoded = xgb_model.predict(match_features)[0]
    proba = xgb_model.predict_proba(match_features)[0]
    pred_label = le.inverse_transform([pred_encoded])[0]
    proba_dict = dict(zip(le.classes_, proba))
    
    pred_proba = proba_dict[pred_label]
    min_expected_odd = round(1 / pred_proba, 2)

    st.subheader("Résultat prévu")
    st.write(f"**Issue prévue :** {pred_label}")
    st.write(f"**Probabilité estimée :** {round(pred_proba * 100, 2)}%")
    st.write(f"**Cote minimale pour value :** {min_expected_odd}")
    
    # Affichage des probabilités complètes
    st.subheader("Probabilités de chaque issue")
    for label, prob in proba_dict.items():
        st.write(f"- **{label}** : {round(prob * 100, 2)}%")

    # Analyse de value bet
    st.subheader("Recommandation de pari")
    if bookmaker_odd == 0:
        st.info("Veuillez entrer une cote proposée par le bookmaker.")
    elif bookmaker_odd > min_expected_odd:
        st.success(f"Value détectée ! Parier sur **{pred_label}** est rentable à cette cote ({bookmaker_odd} > {min_expected_odd})")
    else:
        st.warning(f"Pas de value : la cote ({bookmaker_odd}) est inférieure ou égale à la cote minimale requise ({min_expected_odd}).")
