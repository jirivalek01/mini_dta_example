import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Nastavení cesty k datům (CSV musí být ve stejné složce jako tento soubor)
BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "CEN0203F.csv"

# Načtení dat
df_products = pd.read_csv(DATA_PATH)

# Výběr relevantních sloupců a kopie
df_products_subset = df_products[['Ukazatel', 'Reprezentant', 'CasM', 'Hodnota']].copy()

# Převod sloupce CasM na datetime a seřazení
df_products_subset['CasM'] = pd.to_datetime(df_products_subset['CasM'], errors='coerce')
df_products_subset = df_products_subset.sort_values('CasM')

# Filtr pro Pšenici
df_psenice = df_products_subset[df_products_subset['Reprezentant'].str.contains("Pšenice", na=False)]

# Streamlit titul
st.title("Vizualizace dat zemědělských produktů")

# Graf pro Pšenici
st.subheader("Hodnoty pro Pšenici")
fig_psenice = px.line(df_psenice, x='CasM', y='Hodnota', color='Ukazatel')
st.plotly_chart(fig_psenice, use_container_width=True)

# Filtr pro průměrné ceny
df_products_subset_mean = df_products_subset[df_products_subset['Ukazatel'].str.contains("Průměrná cena", na=False)]

# Graf pro průměrné ceny
st.subheader("Průměrné ceny zemědělských výrobků")
fig_mean = px.line(df_products_subset_mean, x='CasM', y='Hodnota', color='Reprezentant')
st.plotly_chart(fig_mean, use_container_width=True)
