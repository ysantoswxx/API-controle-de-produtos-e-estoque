from fastapi import FastAPI
import funcao


app = FastAPI(title= "Gerenciador de Produtos")


@app.get("/")
def home():
    return{"Mensagem": "Bem-vindo ao Gerenciador de Produtos"}

# -------------------- CADASTRAR PRODUTO --------------------
@app.post("/produtos")
def criar_produtos(nome: str,categoria:str, preco:float, quantidade:int):
    funcao.cadastar_produtos(nome, categoria, preco, quantidade)
    return{"Mensagem": "Produto cadastrado com sucesso!"}

# -------------------- LISTAR PRODUTOS ----------------------
@app.get("/produtos")
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

# -------------------- ATUALIZAR PRODUTO --------------------
@app.put("/produtos/{id_produto}")
def atualizar_produto(id: int, novo_preco: float, nova_quantidade: int):
    produto = funcao.buscar_produto(id)

    if produto:
        funcao.atualizar_produto(id, novo_preco, nova_quantidade)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}


# -------------------- DELETAR PRODUTO ----------------------        
@app.delete("/produtos/{id_produto}")
def deletar_produto(id: int):
    produto = funcao.buscar_produto(id)

    if produto:
        funcao.deletar_produto(id)
        return {"mensagem": "Produto excluído com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}