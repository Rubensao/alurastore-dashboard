import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurar la página
st.set_page_config(page_title="Dashboard AluraStore", layout="wide")

# Título
st.title("📊 Dashboard AluraStore")
st.markdown("Análisis general de las tiendas del Sr. Juan.")

# Cargar datos desde los CSV en GitHub
urls = [
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"
]

# Cargar dataframes
tiendas = [pd.read_csv(url) for url in urls]
nombres_tiendas = [f"Tienda {i+1}" for i in range(4)]

# Métricas clave
st.header("🔍 Métricas Clave")
col1, col2, col3, col4 = st.columns(4)

facturaciones = [df["Precio"].astype(float).sum() for df in tiendas]
calificaciones = [df["Calificación"].mean() for df in tiendas]
envios = [df["Costo de envío"].mean() for df in tiendas]

col1.metric("Mayor Facturación", f"${max(facturaciones):,.2f}")
col2.metric("Menor Facturación", f"${min(facturaciones):,.2f}")
col3.metric("Calificación Promedio Global", f"{sum(calificaciones)/len(calificaciones):.2f}")
col4.metric("Costo Promedio de Envío Global", f"${sum(envios)/len(envios):.2f}")

# Gráfico: Facturación por tienda
st.subheader("💵 Ingresos por Tienda")
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.bar(nombres_tiendas, facturaciones, color='steelblue')
ax1.set_ylabel("USD")
ax1.set_title("Facturación Total por Tienda", loc='center')
ax1.spines[['top', 'right']].set_visible(False)
st.pyplot(fig1)

# Gráfico: Calificación promedio por tienda
st.subheader("⭐ Calificación Promedio por Tienda")
fig2, ax2 = plt.subplots(figsize=(8, 3))
ax2.barh(nombres_tiendas, calificaciones, color='skyblue')
ax2.set_xlabel("Calificación")
ax2.set_title("Calificación por Tienda", loc='center')
ax2.spines[['top', 'right']].set_visible(False)
st.pyplot(fig2)

# Gráfico: Costo de envío por tienda
st.subheader("🚚 Costo Promedio de Envío por Tienda")
fig3, ax3 = plt.subplots(figsize=(8, 3.5))
ax3.plot(nombres_tiendas, envios, marker='o', linestyle='--', color='orange')
ax3.set_ylabel("USD")
ax3.set_title("Costo Promedio por Tienda", loc='center')
ax3.spines[['top', 'right']].set_visible(False)
st.pyplot(fig3)

# Recomendación final
st.markdown("---")
st.success("✅ **Recomendación:** Vender la Tienda 4 por bajo desempeño general (menor facturación, calificación y volumen de ventas).")
