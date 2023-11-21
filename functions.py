  
import streamlit as st
import pandas as pd




    
df = pd.read_csv("./Mall_Customers_Data.csv")  
  
@st.cache_resource
def load_data():
   df = pd.read_csv("./Mall_Customers_Data.csv")
      

    
def mostrar_dataframe():
    st.write(df.head(200))
    
 
    

def analisis_datos():
    import streamlit as st
    from ydata_profiling import ProfileReport
    from streamlit_pandas_profiling import st_profile_report
    import matplotlib 
    import matplotlib.backends.backend_tkagg
    import pandas as pd
  
    

 
    st.write("Analysis of the Data:")
    df = pd.read_csv("./Mall_Customers_Data.csv")  
    profile = ProfileReport(df, title="Profiling Report")
    st_profile_report(profile)       