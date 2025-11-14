import streamlit as st
import requests

#Rodar o streamlit 
# python -m streamlit run app.py

#URL da APi Fastapi
API_URL = "http://127.0.0.1:8000"

st.set_page_config (page_title= "Controle de Estoque", layout="wide", page_icon="🏨")
st.title("📦 Sistema de Controle de Produtos ")

menu = st.sidebar.radio("Menu",
[ "Listar Produtos","Adicionar Produtos", "Atualizar Peço", "Deletar podutos"])

if menu == "Listar Produtos":
    st.subheader("📦 Todos os Produtos")

    response = requests.get(f"{API_URL}/produtos")

    if response.status_code == 200:
        produtos = response.json().get("Produtos",[])


        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nemnhum produto cadastrado ainda!")

    else:
        st.error("Erro ao conectar com a API")