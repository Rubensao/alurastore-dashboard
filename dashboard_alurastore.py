import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración inicial
st.set_page_config(page_title="Dashboard AluraStore", layout="wide")
st.title("📊 Dashboard - Alura Store")

# Cargar datos
@st.cache_data
def cargar_datos():
    urls = [
        "URL_1.csv",
        "URL_2.csv",
        "URL_3.csv",
        "URL_4.csv"
    ]
    return [pd.read_csv(url) for url in urls]

tiendas = cargar_datos()
nombres_tiendas = [f"Tienda {i}" for i in range(1, len(tiendas)+1)]

# Menú de navegación
menu = st.sidebar.radio("Navegación", [
    "📈 Facturación",
    "🛒 Ventas por Categoría",
    "⭐ Calificación Promedio",
    "🔥 Productos Más y Menos Vendidos",
    "🚚 Costo de Envío Promedio"
])

# Opciones
if menu == "📈 Facturación":
    st.header("📈 Facturación Total por Tienda")
    ingresos = [tienda['Precio'].astype(float).sum() for tienda in tiendas]
    for nombre, valor in zip(nombres_tiendas, ingresos):
        st.write(f"{nombre}: ${valor:,.2f}")

    fig, ax = plt.subplots()
    ax.bar(nombres_tiendas, ingresos)
    ax.set_ylabel("USD")
    ax.set_title("Ingresos Totales por Tienda")
    st.pyplot(fig)

elif menu == "🛒 Ventas por Categoría":
    st.header("🛒 Ventas por Categoría")
    for i, tienda in enumerate(tiendas, start=1):
        st.subheader(f"Tienda {i}")
        ventas = tienda.groupby("Categoría del Producto")['Precio'].sum().sort_values(ascending=False)
        st.dataframe(ventas)

elif menu == "⭐ Calificación Promedio":
    st.header("⭐ Calificación Promedio")
    calificaciones = [tienda['Calificación'].mean() for tienda in tiendas]
    st.bar_chart(pd.DataFrame({'Tienda': nombres_tiendas, 'Calificación': calificaciones}).set_index('Tienda'))

elif menu == "🔥 Productos Más y Menos Vendidos":
    st.header("🔥 Productos Más y Menos Vendidos")
    for i, tienda in enumerate(tiendas, start=1):
        st.subheader(f"Tienda {i}")
        productos = tienda.groupby("Producto")["Precio"].sum().sort_values(ascending=False)
        st.write("Más vendidos:")
        st.dataframe(productos.head(3))
        st.write("Menos vendidos:")
        st.dataframe(productos.tail(3))

elif menu == "🚚 Costo de Envío Promedio":
    st.header("🚚 Costo Promedio de Envío por Tienda")
    costos = [tienda['Costo de envío'].mean() for tienda in tiendas]
    st.write(pd.DataFrame({'Tienda': nombres_tiendas, 'Costo Promedio': costos}).set_index('Tienda'))
    st.bar_chart(pd.DataFrame({'Tienda': nombres_tiendas, 'Costo Promedio': costos}).set_index('Tienda'))
