import pandas as pd
import requests
import streamlit as st
# Carregar o arquivo CSV
df = pd.read_csv('ordenado.csv')
top_10_ids = df['ID'].value_counts().head(10).index.tolist()
# Função para obter informações de um filme pelo ID
def get_movie_info(movie_id):
    url = f"https://api.letterboxd.com/api/v0/films/{movie_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        return None
 
df = pd.read_csv('country.csv')
pais=st.selectbox("países", df ['country'])
st.write(df[df['country'] == pais])

filtered_movies = df[df['country'] == selected_country]

# Display filtered movies
st.write(filtered_movies)

# Count movies per category
category_counts = filtered_movies['genre.1'].value_counts()

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel('Category')
plt.ylabel('Number of Movies')
plt.title(f'Number of Movies per Category in {selected_country}')
plt.xticks(rotation=45, ha='right')
st.pyplot()
