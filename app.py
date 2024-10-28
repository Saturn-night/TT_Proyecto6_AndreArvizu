import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') 
st.header("Analisis de vehiculos")
hist_button = st.button('Construir histograma') 
        
if hist_button: 
     
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.histogram(car_data, x="odometer")
        
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir grafico de dispercion') 

if scatter_button: 
     
    st.write('Creación de un grafico de dispercion para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.scatter(car_data, x="odometer",y="price")
        
    st.plotly_chart(fig, use_container_width=True)