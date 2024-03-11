import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

actors = [
    {
        'id': 1,
        'name': 'Stallone'
    },
    {
        'id': 2,
        'name': 'The Rock'
    },
    {
        'id': 3,
        'name': 'Dante'
    },
]

def show_actors():
    st.write('Lista de Atores')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )

    st.title('Cadastrar novo Ator')
    name = st.text_input('Nome do Ator')
    if st.button('Cadastrar'):
        st.success(f'Ator "{name}" cadastrado com sucesso')

