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

#df_country = pd.read_csv('country.csv')
#pais=st.selectbox("países", df ['country'])
#st.write(df[df['country'] == pais])

pais = st.selectbox("Países", df['country'].unique())
genero = st.selectbox("Gênero", df.sort_values(by='genre.1')['genre.1'].unique())
lingua = st.selectbox("Língua ", df.sort_values(by='language.1')['language.1'].unique())

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

# Novo código para exibir os 10 filmes mais bem avaliados
st.write("Top 10 filmes mais bem avaliados:")

# Verificar se as colunas estão presentes no DataFrame
required_columns = ['ID', 'title', 'five.star']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Erro: As seguintes colunas estão faltando no DataFrame: {', '.join(missing_columns)}")
else:
    top_10_filmes = df.nlargest(10, 'five.star')
    st.dataframe(top_10_filmes[['ID', 'title', 'five.star']])

