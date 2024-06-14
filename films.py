import pandas as pd
import requests
import streamlit as st
import matplotlib.pyplot as plt

# Function to get movie info by ID
def get_movie_info(movie_id):
    url = f"https://api.letterboxd.com/api/v0/films/{movie_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        return None

# Load movie data
df_movies = pd.read_csv('ordenado.csv')

# Load country data
df_countries = pd.read_csv('country.csv')

# Create Streamlit app
st.title('Movie Information by Country')

# Dropdown to select country
selected_country = st.selectbox("Select a country", df_countries['country'])

# Filter movies by selected country
filtered_movies = df_movies[df_movies['country'] == selected_country]

# Display filtered movies
st.write(filtered_movies)

# Count movies per category
category_counts = filtered_movies['category'].value_counts()

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel('Category')
plt.ylabel('Number of Movies')
plt.title(f'Number of Movies per Category in {selected_country}')
plt.xticks(rotation=45, ha='right')
st.pyplot()

