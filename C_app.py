import streamlit as st
import pandas as pd 
from functions import mostrar_dataframe, analisis_datos

st.sidebar.title("Select an option")
page = st.sidebar.selectbox("Explore or predict", ("Explore Data", "Analize Data")) 


if page =="Explore Data":
    mostrar_dataframe()
    

if page =="Analize Data":
    analisis_datos()
     
    
    
    
    
