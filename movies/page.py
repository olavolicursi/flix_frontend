import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

movies = [
    {
        'id': 1,
        'name': 'De volta para o futuro'
    },
    {
        'id': 2,
        'name': 'Interestellar'
    },
    {
        'id': 3,
        'name': 'Star Wars'
    },
]

def show_movies():
    st.write('Lista de Filmes')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )

    st.title('Cadastrar novo Filme')
    name = st.text_input('Nome do Filme')
    if st.button('Cadastrar'):
        st.success(f'Filme "{name}" cadastrado com sucesso')

