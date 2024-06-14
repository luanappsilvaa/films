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
selected_country = st.selectbox("Países", countries_df['country'])
print("País selecionado:", selected_country)  # Adicionado para depuração

# Verificar se o país foi selecionado
if selected_country:
    # Filtrar os filmes pelo país selecionado
    filtered_movies = df[df['country'] == selected_country]
    print("Número de filmes após filtragem:", len(filtered_movies))  # Adicionado para depuração

    # Exibir os filmes filtrados
    st.write(filtered_movies)

    # Contar filmes por categoria
    category_counts = filtered_movies['genre'].value_counts()

    # Plotar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(category_counts.index, category_counts.values)
    plt.xlabel('Categoria')
    plt.ylabel('Número de Filmes')
    plt.title(f'Número de Filmes por Categoria em {selected_country}')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()
else:
    st.write("Nenhum país selecionado. Por favor, selecione um país.")
