import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "CEN0203F.csv"

df = pd.read_csv(DATA_PATH)

df = df[['Ukazatel', 'Reprezentant', 'CasM', 'Hodnota']].copy()
df['CasM'] = pd.to_datetime(df['CasM'], errors='coerce')
df = df.sort_values('CasM')

df_psenice = df[df['Reprezentant'].str.contains("Pšenice", na=False)]

fig = px.line(df_psenice, x='CasM', y='Hodnota', color='Ukazatel')

st.plotly_chart(fig, use_container_width=True)
