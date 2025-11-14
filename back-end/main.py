from fastapi import FastAPI
import funcao


app = FastAPI(title= "Gerenciador de Produtos")


@app.get("/")
def home():
    return{"Mensagem": "Bem-vindo ao Gerenciador de Produtos"}

# -------------------- CADASTRAR PRODUTO --------------------
@app.post("/produtos")
def criar_protudo(nome: str,categoria:str, preco:float, quantidade:int):
    funcao.cadrastar_produtos(nome, categoria, preco, quantidade)
    return{"Mensagem": "Produto cadastrado com sucesso!"}

# -------------------- LISTAR PRODUTOS ----------------------
@app.post("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    listar = []

    for linha in produtos:
        listar.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
    
    return{"produtos": listar}