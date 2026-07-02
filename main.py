import streamlit as st

from utils.dados import carregar_dataset, tratamento_dados
from utils.pesquisa import encontrar_filme



# Configuração da página web
st.set_page_config(
    page_title='Find IMDB Movies',
    page_icon='🎬',
    layout='wide'
)

st.title('Motor de Busca para Filmes do IMDB 🎬')
st.subheader('Encontra o filme que tanto procuras mesmo sem saber o nome completo! 🕵', divider='rainbow',)

# Carregar o dataset
@st.cache_data
def carregar_dados_cache(path):
    df = carregar_dataset(path)
    df = tratamento_dados(df)

    return df

path_df = 'data/top_1000_imdb_movies.csv'
df_tratado = carregar_dados_cache(path_df)

# Continuação da configuração da página web
st.markdown('')

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "similaridade" not in st.session_state:
    st.session_state.similaridade = 50

if "limite" not in st.session_state:
    st.session_state.limite = 5

user_input = st.text_input(
    "De que filme estás à procura? 🔎",
    key="user_input"
    )

similaridade = st.slider(
    "Seleciona a percentagem mínima de semelhança 👀",
    min_value=0, 
    max_value=100, 
    key="similaridade"
    )

limite = st.slider(
    "Seleciona a quantidade de resultados que queres ver 🎯", 
    min_value=1, 
    max_value=10,
    key="limite"
    )

st.markdown("*Nota: O número de resultados é menor, quanto maior for o valor de semelhança.*")

# Imprimir os resultados
# Cada resultado tem informação adicional, que pode ser expandida

if user_input:
    resultados = encontrar_filme(df_tratado, user_input, limite, similaridade)
    st.markdown("#### **Resultados:**")
    if resultados:
        for filme in resultados:
            with st.expander(f"✅ {filme['titulo']} ({filme['ano']}) - Semelhança: {filme['semelhanca']:.2f}%"):
                st.write(f"⏳ **Duração:** {filme['duracao']} min")
                st.write(f"⭐️ **Rating:** {filme['rating']}")
                st.write(f"📖 **Sinopse:** {filme['sinopse']}")
    else:
        st.write("Não foram encontradas correspondências ☹️")

# Adicionar um botão RESET
def reset():
    st.session_state.user_input = ""
    st.session_state.similaridade = 50
    st.session_state.limite = 5

st.button("🔄 RESET", on_click=reset)

st.caption("*Este projeto foi desenvolvido com Streamlit*", text_alignment='center')