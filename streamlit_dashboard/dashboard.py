import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Business Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# Título y descripción
st.title("Business Intelligence Dashboard")
st.markdown("""
    Este dashboard muestra información analítica clave de tu negocio.
    Los datos presentados aquí son actualizados periódicamente y pueden filtrarse según tus necesidades.
""")

# Sidebar para filtros
st.sidebar.header("Filtros")
fecha_inicio = st.sidebar.date_input("Fecha de inicio", pd.to_datetime("2024-01-01"))
fecha_fin = st.sidebar.date_input("Fecha de fin", pd.to_datetime("2025-04-16"))
categoria = st.sidebar.selectbox("Categoría", ["Todas", "Ventas", "Marketing", "Operaciones"])

# Datos de ejemplo (en un proyecto real, esto vendría de tu base de datos Django)
# Simulamos algunos datos
np.random.seed(42)
fechas = pd.date_range(start="2024-01-01", end="2025-04-16")
datos = {
    "fecha": np.random.choice(fechas, 500),
    "ventas": np.random.randint(100, 10000, 500),
    "costos": np.random.randint(50, 5000, 500),
    "categoria": np.random.choice(["Ventas", "Marketing", "Operaciones"], 500)
}
df = pd.DataFrame(datos)

# Filtrar los datos según los filtros
df_filtrado = df[
    (df["fecha"] >= pd.Timestamp(fecha_inicio)) &
    (df["fecha"] <= pd.Timestamp(fecha_fin))
]

if categoria != "Todas":
    df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria]

# Crear varias columnas para mostrar KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Ventas", f"${df_filtrado['ventas'].sum():,.0f}", "+12%")

with col2:
    st.metric("Total Costos", f"${df_filtrado['costos'].sum():,.0f}", "-5%")

with col3:
    ganancia = df_filtrado['ventas'].sum() - df_filtrado['costos'].sum()
    st.metric("Ganancia", f"${ganancia:,.0f}", "+20%")

with col4:
    margen = ganancia / df_filtrado['ventas'].sum() * 100 if df_filtrado['ventas'].sum() > 0 else 0
    st.metric("Margen", f"{margen:.1f}%", "+2.5%")

# Gráficos
st.subheader("Análisis de Ventas y Costos")
fig, ax = plt.subplots(figsize=(10, 6))
df_agrupado = df_filtrado.groupby(df_filtrado["fecha"].dt.month_name()).agg({
    "ventas": "sum",
    "costos": "sum"
}).reset_index()

# Ordenar por mes
meses_orden = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]
df_agrupado["fecha"] = pd.Categorical(df_agrupado["fecha"], categories=meses_orden, ordered=True)
df_agrupado = df_agrupado.sort_values("fecha")

st.bar_chart(df_agrupado.set_index("fecha")[["ventas", "costos"]])

# Tabla de datos
st.subheader("Datos Detallados")
st.dataframe(df_filtrado[["fecha", "ventas", "costos", "categoria"]].sort_values("fecha"))

# Sección de análisis avanzado
st.subheader("Análisis Avanzado")
tabs = st.tabs(["Tendencias", "Distribución", "Predicciones"])

with tabs[0]:
    st.line_chart(df_filtrado.groupby(df_filtrado["fecha"].dt.to_period("W")).agg({"ventas": "mean"}).reset_index().set_index("fecha"))
    st.markdown("Este gráfico muestra las tendencias semanales de ventas durante el período seleccionado.")

with tabs[1]:
    fig, ax = plt.subplots()
    ax.hist(df_filtrado["ventas"], bins=20)
    ax.set_xlabel("Ventas")
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)
    st.markdown("Este histograma muestra la distribución de las ventas en el período seleccionado.")

with tabs[2]:
    st.info("Las predicciones de ventas futuras se basarán en los datos históricos y tendencias actuales.")
    # Aquí podrías implementar algún modelo predictivo simple