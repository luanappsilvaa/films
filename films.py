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
body {
background-image: url("https://www.google.com/imgres?q=sala%20de%20cinema%20desenho&imgurl=https%3A%2F%2Fst3.depositphotos.com%2F6064568%2F13346%2Fv%2F450%2Fdepositphotos_133463728-stock-illustration-interior-of-a-cinema-movie.jpg&imgrefurl=https%3A%2F%2Fdepositphotos.com%2Fbr%2Fvectors%2Ffundo-cinema.html&docid=e5vyEQSTg14PRM&tbnid=bya9j7u0TlomRM&vet=12ahUKEwim7aSq_uKGAxXclJUCHRFNB0AQM3oECH4QAA..i&w=600&h=424&hcb=2&ved=2ahUKEwim7aSq_uKGAxXclJUCHRFNB0AQM3oECH4QAA");
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

# Nova funcionalidade: Top 10 filmes mais bem avaliados
st.write("Top 10 Filmes Mais Bem Avaliados")

# Filtrar os dados pelo país selecionado
filmes_por_pais = df[df['country'] == pais]
df[(df['country']==pais)&(df['language.1']==lingua)&(df['genre.1']==genero)]


# Contar a quantidade de filmes por categoria

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


