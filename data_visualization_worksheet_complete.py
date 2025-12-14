import pandas as pd

df_products = pd.read_csv("/CEN0203F.csv")

df_products.head()

df_products['Ukazatel'].unique()

df_products['IndicatorType'].unique()

df_products['Reprezentant'].unique()

import pandas as pd
df_products = pd.read_csv("/CEN0203F.csv")
df_products_subset = df_products[['Ukazatel','Reprezentant','CasM','Hodnota']].copy()

df_products_subset.info()

df_products_subset.describe()

df_psenice = df_products_subset[df_products_subset['Reprezentant']=='Pšenice potravinářská [t]']

df_psenice.head()

import plotly.express as px

fig = px.line(df_psenice, x='CasM', y='Hodnota', color='Ukazatel')

fig.show()

df_products_subset_mean = df_products_subset[df_products_subset['Ukazatel']=='Průměrná cena zemědělských výrobků (Kč)']

fig_mean = px.line(df_products_subset_mean, x='CasM', y='Hodnota', color='Reprezentant')
fig_mean.show()