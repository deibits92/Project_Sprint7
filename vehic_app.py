import streamlit as st
import pandas as pd
import plotly.graph_objects as go

#Lectura de base de datos en csv y asignado a df
vehic_data=pd.read_csv('vehicles_us.csv')

#Encabezado para la aplicación
st.header("Análisis de Datos Vehiculares en EE.UU.")

#Botón para crear gráfico en la aplicación
hist_button = st.button('Graficar en modo Histograma')

#Botón para crear gráfico de dispersión en la aplicación
scatter_button = st.button('Graficar en modo Dispersión')

# Lógica cuando se presiona el botón para histograma
if hist_button:
    st.write("Generación de histograma para el conjunto de datos")
    
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=vehic_data['odometer'])])

    # Incluir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución de Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Lógica cuando se presiona el botón para gráfico de dispersión
if scatter_button:
    st.write("Generación de gráfico de dispersión para el conjunto de datos")
    
    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de dispersión
    fig = go.Figure(data=go.Scatter(x=vehic_data['year'], y=vehic_data['price'], mode='markers'))

    # Incluir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Año y precio de Vehículos',
                      xaxis_title='Año',
                      yaxis_title='Precio (USD)')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
