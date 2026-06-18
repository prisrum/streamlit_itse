import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título e introducción visibles en la app
st.title("Explorador de Pingüinos")
st.write("Distribución del largo del pico según la especie seleccionada.")

# Carga del dataset desde la web
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)
df = df.dropna()

# Widget: menú desplegable — la elección del usuario queda en 'especie'
especie = st.selectbox("Seleccioná una especie:", df["species"].unique())

# Filtrado reactivo: se recalcula cada vez que cambia la selección
datos_filtrados = df[df["species"] == especie]

# Gráfico que refleja los datos filtrados
fig, ax = plt.subplots()
ax.hist(datos_filtrados["bill_length_mm"], bins=15,
        color="steelblue", edgecolor="white")
ax.set_xlabel("Largo del pico (mm)")
ax.set_ylabel("Frecuencia")
ax.set_title(f"Distribución del pico — {especie}")
st.pyplot(fig)

# Métrica resumen con formato destacado
st.metric("Promedio del pico (mm)",
          round(datos_filtrados["bill_length_mm"].mean(), 2))