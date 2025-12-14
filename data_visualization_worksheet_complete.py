


import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Nastavení cesty k datům
BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "CEN0203F.csv"

# Načtení dat
df = pd.read_csv(DATA_PATH)
df['CasM'] = pd.to_datetime(df['CasM'], errors='coerce')

st.title("🌾 Dashboard zemědělských produktů")

# Sidebar pro výběr reprezentanta
reprezentant_list = df['Reprezentant'].unique()
selected_reprezentant = st.sidebar.selectbox("Vyber produkt", reprezentant_list)

# Sidebar pro výběr ukazatele
ukazatel_list = df['Ukazatel'].unique()
selected_ukazatel = st.sidebar.selectbox("Vyber ukazatel", ukazatel_list)

# Filtrace dat
df_filtered = df[(df['Reprezentant'] == selected_reprezentant) &
                 (df['Ukazatel'] == selected_ukazatel)]

st.subheader(f"📈 Časová řada pro {selected_reprezentant} ({selected_ukazatel})")

# Graf
fig = px.line(df_filtered, x='CasM', y='Hodnota', title=f"{selected_ukazatel} - {selected_reprezentant}",
              markers=True, template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

# Zobrazení tabulky
st.subheader("Tabulka dat")
st.dataframe(df_filtered)
