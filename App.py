import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from functions import Main_page,show_dataframe, analisis_datos,Clustering

#Page Setup

st.set_page_config(page_title="Mall Customers Segmentation Dashboard Application")
st.title("Mall Customer Segmentation Dashboard Application")



#sidebar menu
import streamlit as st
with st.sidebar:
    selected = option_menu("Select an Option", ["Main Page", "Explore Data", "Analize Data", "Customer Clusters"], 
        icons=['house', 'search','graph-up-arrow','clipboard-data'], menu_icon="menu-down", default_index=1)
    selected
  
#
if selected == "Main Page":
    Main_page()

if selected =="Explore Data":
    show_dataframe()
    

if selected =="Analize Data":
    analisis_datos()
    
    
if selected == "Customer Clusters":
    Clustering()
    
    
    
        
     
    
    
    
    
