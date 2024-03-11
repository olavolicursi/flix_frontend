import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 4
    },
    {
        'id': 3,
        'stars': 4
    },
]

def show_reviews():
    st.write('Lista de reviews')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
    )

    st.title('Cadastrar novo review')
    stars = st.text_input('Review')
    if st.button('Cadastrar'):
        st.success(f'review "{stars}" cadastrado com sucesso')

