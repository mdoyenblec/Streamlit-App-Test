import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Airbnb Paris Analyse de marché V2')
st.title('Hello')

DATA_URL = ('http://data.insideairbnb.com/france/ile-de-france/paris/2023-09-04/visualisations/listings.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Chargement des données...')
data = load_data(10000)
data_load_state.text("Fait! (using st.cache)")

if st.checkbox('Afficher les données raw'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Prix Moyen à Paris')
average_price_paris = data['price'].mean()
st.write(f"Le prix moyen à Paris est de {average_price_paris:.2f} €")

st.subheader('Prix Moyen par Quartier (Interactif)')
average_price_per_neighborhood = data.groupby('neighbourhood')['price'].mean().reset_index()
fig = px.bar(average_price_per_neighborhood, x='neighbourhood', y='price', 
             labels={'price': 'Prix Moyen', 'neighbourhood': 'Quartier'},
             title="Prix Moyen par Quartier à Paris")
st.plotly_chart(fig)

st.subheader('Nombre de biens par Quartier')
count_per_neighborhood = data['neighbourhood'].value_counts()
fig = px.bar(count_per_neighborhood, x='id', y='neighbourhood', 
             labels={'id': 'Listings', 'neighbourhood': 'Quartier'},
             title="Nombre de biens par Quartier à Paris")
st.plotly_chart(fig)


st.subheader('Carte Dynamique avec Prix des Logements')
st.map(data)

st.subheader('Nombre de Logements par Propriétaire')
properties_per_owner = data['host_name'].value_counts().head(10)  
st.bar_chart(properties_per_owner)



        