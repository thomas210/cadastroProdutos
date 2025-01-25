import streamlit as st
import pandas as pd

# Inicializar um DataFrame para armazenar os produtos cadastrados
if 'produtos' not in st.session_state:
    st.session_state.produtos = pd.DataFrame(columns=["Nome", "Marca", "Valor", "Quantidade em Estoque"])

# Função para adicionar um novo produto ao DataFrame
def adicionar_produto(nome, marca, valor, quantidade):
    novo_produto = pd.DataFrame([[nome, marca, valor, quantidade]], columns=["Nome", "Marca", "Valor", "Quantidade em Estoque"])
    st.session_state.produtos = pd.concat([st.session_state.produtos, novo_produto], ignore_index=True)

# Título
st.title('Cadastro de Produtos')

# Formulário para adicionar novos produtos
with st.form(key='cadastro_produto'):
    nome = st.text_input('Nome do Produto')
    marca = st.text_input('Marca')
    valor = st.number_input('Valor', min_value=0.0, format="%.2f")
    quantidade = st.number_input('Quantidade em Estoque', min_value=0)

    # Botão para submeter o formulário
    submitted = st.form_submit_button('Cadastrar Produto')
    
    if submitted:
        adicionar_produto(nome, marca, valor, quantidade)
        st.success(f'Produto "{nome}" cadastrado com sucesso!')

# Mostrar todos os produtos cadastrados
st.subheader('Produtos Cadastrados')
st.dataframe(st.session_state.produtos)
