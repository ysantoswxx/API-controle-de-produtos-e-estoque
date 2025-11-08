from fastapi import FastAPI
import funcao


app = FastAPI(title= "Gerenciador de Produtos")


@app.get("/")
def home():
    return{"Mensagem": "Bem-vindo ao Gerenciador de Produtos"}


@app.post("/produtos")
def criar_protudo(nome: str,categoria:str, preco:float, quantidade:int):
    funcao.cadrastar_produtos(nome, categoria, preco, quantidade)
    return{"Mensagem": "Produto cadastrado com sucesso!"}