import pandas as pd
import requests

# Carregar o arquivo CSV
df = pd.read_csv('ordenado.csv')

# Ordenar o DataFrame pelos ratings em ordem decrescente
df_sorted = df.sort_values(by='averageRating', ascending=False)

# Obter os IDs dos 10 filmes melhor classificados
top_10_ids = df_sorted['ID'].head(10).tolist()

# Função para obter informações de um filme pelo ID
def get_movie_info(movie_id):
    url = f"https://api.letterboxd.com/api/v0/films/{movie_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        return None

# Lista para armazenar informações dos 10 filmes melhor classificados
top_10_movies_info = []

# Obter informações dos 10 filmes melhor classificados
for movie_id in top_10_ids:
    movie_info = get_movie_info(movie_id)
    if movie_info:
        top_10_movies_info.append(movie_info)

# Imprimir informações dos 10 filmes melhor classificados
for movie_info in top_10_movies_info:
    print("Título:", movie_info['title'])
    print("Avaliação:", movie_info['averageRating'])
    print("Resumo:", movie_info['shortDescription'])
    print("Dados do filme:", movie_info['tags'])
    print("="*50)

# Salvar as informações em um arquivo .txt
with open('top_10_rated_movies_info.txt', 'w', encoding='utf-8') as file:
    for movie_info in top_10_movies_info:
        file.write("Título: " + movie_info['title'] + "\n")
        file.write("Avaliação: " + str(movie_info['averageRating']) + "\n")
        file.write("Resumo: " + movie_info['shortDescription'] + "\n")
        file.write("Dados do filme: " + str(movie_info['tags']) + "\n")
        file.write("="*50 + "\n")
