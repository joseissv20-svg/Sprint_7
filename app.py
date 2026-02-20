import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')
#Creamos el titulo de la aplicación Streamlit
st.title('Análisis de anuncios de venta de coches')
#Colocamos un titulo para la sección de visualización de datos
st.header('Visualización de datos')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')
#Crear un boton en la aplicación Streamlit que cree un grafico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
#Lógica a ejecutar cuando se hace clic en el botón de gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig_scatter = go.Figure(data=go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers'))
    fig_scatter.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig_scatter, use_container_width=True)

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)