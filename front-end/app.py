import streamlit as st
import requests

#Rodar o streamlit 
# python -m streamlit run app.py

#URL da APi Fastapi
API_URL = "http://127.0.0.1:8000"

st.set_page_config (page_title= "Controle de Estoque", layout="wide", page_icon="🏨")
st.title("📦 Sistema de Controle de Produtos ")

menu = st.sidebar.radio("Menu",
[ "Listar Produtos","Adicionar Produtos", "Atualizar Produtos", "Deletar Podutos"])

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


elif menu == "Adicionar Produtos":
    st.subheader("📝Adicionar Novo Produto")

    nome = st.text_input("Nome")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade", min_value=0, step=1)

    
    if st.button("Cadastrar"):
        if nome and categoria:
            params = {
                "nome": nome,
                "categoria": categoria,
                "preco": preco,
                "quantidade": quantidade,
            }
    
            response = requests.post(f"{API_URL}/produtos", params=params)

            if response.status_code ==  200:
                st.success("Produtos adicionado com sucesso!")

            else:
                st.error("Erro ao adicionar o produto")

    else:
        st.warning("Preencha todos os campos obrigatórios!") 

elif menu == "Atualizar Produtos":
    st.subheader("✏ Atualizar Produtos")

    id_produtos = st.number_input("ID do Produto", min_value=1, step=1)
    novo_preco = st.number_input("Novo preço", min_value=0.0, format="%.2f")
    nova_quantidade = st.number_input("Nova Quantidade", min_value=0, step=1)

    if st.button("Atualizar"):
        params = {
            "novo_preco": novo_preco,
            "nova_quantidade": nova_quantidade
    }
        response = requests.put(f"{API_URL}/produtos/ {id}",params=params)

        if response.status_code == 200:
            msg = response.json()
            st.success(msg.get("Mensagem", "Produtos atualizado!"))
        else: 
            st.error("Erro ao atualizar o produto")


elif menu == "Deletar Podutos":
    st.subheader("🗑 Deletar Produtos")

    id_produtos = st.number_input("ID do produto", min_value=1, step=1)

    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/podutos/{id_produtos}")

        if response .status_code == 200:
            msg = response.json()
            if "erro" in msg:
                st.warning(msg["erro"])
            else:
                st.success(msg["mensagem"])
        else:
            st.error("Erro ao deletar produto.")

