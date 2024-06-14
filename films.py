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
 
df_country = pd.read_csv('country.csv')
pais=st.selectbox("países", df ['country'])
st.write(df[df['country'] == pais])

pais = st.selectbox("Países", df_country['country'].unique())
st.write(df_paises[df_country['country'] == pais])

# Filtrar os dados pelo país selecionado
filmes_por_pais = df_country[df_country['country'] == pais]

# Contar a quantidade de filmes por categoria
contagem_categorias = filmes_por_pais['category'].value_counts()

# Plotar o gráfico
st.write("Quantidade de filmes por categoria no país selecionado:")
fig, ax = plt.subplots()
sns.barplot(x=contagem_categorias.index, y=contagem_categorias.values, ax=ax)
ax.set_xlabel('Categoria')
ax.set_ylabel('Quantidade de Filmes')
ax.set_title('Quantidade de Filmes por Categoria')
plt.xticks(rotation=45)
st.pyplot(fig)
