import pandas as pd
import requests
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

# CSS para a imagem de fundo
page_bg_img = '''
<style>
.stApp {
  background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fbr.freepik.com%2Fvetores-premium%2Fsala-de-cinema-com-tela-vazia_6331364.htm&psig=AOvVaw1N_fYkHQgeyDjEDjdo3IGo&ust=1718719918044000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPjKrerV4YYDFQAAAAAdAAAAABAE ");
  background-size: cover;
}
</style>
'''

# Inserir o CSS no Streamlit
st.markdown(page_bg_img, unsafe_allow_html=True)

# Inserir o nome do site
st.title("TOP10FILMS")

# Seção de seleção de filtros
pais = st.selectbox("Países", df['country'].unique())
genero = st.selectbox("Gênero", df.sort_values(by='genre.1')['genre.1'].unique())
lingua = st.selectbox("Língua", df.sort_values(by='language.1')['language.1'].unique())

# Filtrar os dados pelo país selecionado
filmes_por_pais = df[df['country'] == pais]
fimes_por_genero = filmes_por_pais

# Contar a quantidade de filmes por categoria
contagem_categorias = filmes_por_pais['genre.1'].value_counts()

# Plotar o gráfico
st.write("Quantidade de filmes por categoria no país selecionado:")
fig, ax = plt.subplots()
sns.barplot(x=contagem_categorias.index, y=contagem_categorias.values, ax=ax)
ax.set_xlabel('Categoria')
ax.set_ylabel('Quantidade de Filmes')
ax.set_title('Quantidade de Filmes por Categoria')
plt.xticks(rotation=45)
st.pyplot(fig)

# Nova funcionalidade: Top 10 filmes mais bem avaliados
st.write("Top 10 Filmes Mais Bem Avaliados")
