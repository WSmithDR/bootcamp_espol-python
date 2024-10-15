import streamlit as st
import pandas as pd
import plotly.express as px
import utils

# Título de la aplicación
st.title('Mini Proyecto de Análisis de Datos con Streamlit')

# Subida de archivos
uploaded_file = st.file_uploader("Elige un archivo CSV o TSV", type=["csv", "tsv"])

# Cargar el archivo
if uploaded_file is not None:
    # Leer archivo según su extensión
    if uploaded_file.name.endswith('.csv'):
        # df = pd.read_csv(uploaded_file)
        df = utils.cargar_csv(uploaded_file)
    elif uploaded_file.name.endswith('.tsv'):
        # df = pd.read_csv(uploaded_file, sep='\t')
        df = utils.cargar_tsv(uploaded_file)

    # Mostrar los primeros datos del archivo cargado
    st.write("Vista previa de los datos:")
    st.dataframe(utils.cargar_cabecera(df))

    # Selección de columnas para análisis
    columnas = utils.obtener_columnas(df)
    columna_x = st.selectbox('Selecciona una columna para el eje X', columnas)
    columna_y = st.selectbox('Selecciona una columna para el eje Y (opcional)', columnas + [None], index=len(columnas))

    # Gráfico interactivo con Plotly
    if columna_y:
        fig = px.scatter(df, x=columna_x, y=columna_y, title=f'Dispersión entre {columna_x} y {columna_y}')
    else:
        fig = px.histogram(df, x=columna_x, title=f'Histograma de {columna_x}')
    
    # Mostrar el gráfico
    st.plotly_chart(fig)

    # Estadísticas básicas
    st.write(f"Resumen estadístico de la columna {columna_x}:")
    st.write(utils.obtener_estadistica_basica(df,columna_x))

    # datos atipicos
    st.write(f"Resumen estadístico de la columna {columna_x}:")
    st.write(utils.encontrar_peliculas_con_valores_atipicos())

    # peliculas por genero
    df_genero_peliculas = utils.obtener_cantidad_peliculas_por_genero()
    fig_genero = px.bar(df_genero_peliculas, x='genres', y='cantidad', title='Cantidad de Películas por Género')
    st.plotly_chart(fig_genero)

    # peores peliculas por rating
    df_genero_peliculas = utils.obtener_top_5_peliculas_con_mas_bajo_rating()
    st.write(f"Resumen Peores peliculas:")
    st.write(df_genero_peliculas)

    # Slider de fecha
    if df[columna_x].dtype in ['int64', 'float64']:
        valor_min = st.slider(f"Elige un valor mínimo para {columna_x}", float(df[columna_x].min()), float(df[columna_x].max()))
        df_filtrado = df[df[columna_x] >= valor_min]
        st.write(f"Filtrado por {columna_x} mayor o igual a {valor_min}:")
        st.dataframe(df_filtrado.head())

else:
    st.write("Por favor, sube un archivo para comenzar el análisis.")