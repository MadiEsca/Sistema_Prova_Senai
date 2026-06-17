import streamlit as st
import backend.connection as ct
import pandas as pd
import time

# Configurações
st.write("Funciona")

#Criando um formulário
with st.form("formulario_cadastro"):
  st.write("Fomulário de teste de cadastro")
  nome_produto = st.text_input("Digite o nome do produto",placeholder="Eg. Sacola de lixo")
  valor_unitario_produto = st.number_input("Digite o preço do produto: ", placeholder="Eg. 21", min_value=0.00)
  quantidade_produto = st.number_input("Digite a quantidade de produtos: ", 
                                      placeholder="Eg. 3",
                                      min_value=0,
                                      max_value=100)
  categoria_produto = st.selectbox('Escolha uma categoria', ['Higiene','Quimico','Perecivel'])
  enviar = st.form_submit_button('Realizar cadastro')
  
  if enviar:
    try:
      ct.create_product(quantidade=quantidade_produto, 
                        categoria_escolhida=categoria_produto, 
                       nome=nome_produto,
                       valor_unitario=valor_unitario_produto)
      st.success("Usuário criado com sucesso")
    except Exception as error:
      st.error(f"Não foi possível realizar o cadastro: {error}")


## Add a selectbox to the sidebar:
#add_selectbox = st.sidebar.selectbox(
#    'How would you like to be contacted?',
#    ('Email', 'Home phone', 'Mobile phone')
#)
#
## Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
#    'Select a range of values',
#    0.0, 100.0, (25.0, 75.0)
#)
#
#'Starting a long computation...'
#
## Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)
#
#for i in range(100):
#  # Update the progress bar with each iteration.
#  latest_iteration.text(f'Iteration {i+1}')
#  bar.progress(i + 1)
#  time.sleep(0.1)
#
#'...and now we\'re done!'