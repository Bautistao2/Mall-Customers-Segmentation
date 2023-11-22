  
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
from kneed import KneeLocator
import seaborn as sns

    
df = pd.read_csv("./Mall_Customers_Data.csv")  
X = df.iloc[:, [3,4]].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
wcss=[]
for i in range(1,15):
    kmeans = KMeans(n_clusters=i, init = 'k-means++', random_state=0)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
kneedle = KneeLocator(range(1,15),wcss,curve = 'convex', direction = 'decreasing')
elbow_point = kneedle.elbow    
kmeansmodel = KMeans(n_clusters = elbow_point, init = 'k-means++' , random_state=0)
y_kmeans = kmeansmodel.fit_predict(X)   
kmeans = pd.DataFrame(y_kmeans)
dataset_1 = pd.concat([df,kmeans],axis=1)
labels = kmeansmodel.labels_
b = df.copy()
b['Cluster'] = labels



  
@st.cache_resource
def load_data():
   df = pd.read_csv("./Mall_Customers_Data.csv")
   X = df.iloc[:, [3,4]].values
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   wcss=[]
   for i in range(1,15):
        kmeans = KMeans(n_clusters=i, init = 'k-means++', random_state=0)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)
   kmeansmodel = KMeans(n_clusters = elbow_point, init = 'k-means++' , random_state=0)
   y_kmeans = kmeansmodel.fit_predict(X)   
   kmeans = pd.DataFrame(y_kmeans)
   dataset_1 = pd.concat([df,kmeans],axis=1)
   labels = kmeansmodel.labels_
   b = df.copy()
   b['Cluster'] = labels
   return(b)
   
df1 = load_data 
   

def Main_page():
    with open("./images/Client-segmentation.png", "rb") as file:
        imagen_data = file.read()
        st.image(imagen_data)
        
    
    st.write("By  Osthailyd Bautista")    
      

    
def show_dataframe():
    st.write("## Data of the Customers")
    st.write(b)
    
   

def analisis_datos():
    import streamlit as st
    from ydata_profiling import ProfileReport
    from streamlit_pandas_profiling import st_profile_report
    import matplotlib 
    import matplotlib.backends.backend_tkagg
    import pandas as pd
  

    st.write("## Analysis of the Data:")
    profile = ProfileReport(b,  title="Profiling Report")
    st_profile_report(profile)       
    

def Clustering():
   fig1=sns.pairplot(b,hue='Cluster',palette="Spectral")
   st.write("## Different Customer Characteristics Based on Clusters")
   st.pyplot(fig1)
    
 
 


    
    