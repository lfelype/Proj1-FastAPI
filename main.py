from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#Home
@app.get("/")
def raiz ():
    return {"Ola Mundo, bem vindo a nossa Home!"}


#CriandoModelo
class Usuario(BaseModel):
    id: int
    email: str
    senha: str

#CriandoBaseDeDados
base_de_dados = [
    Usuario(id=1, email = "us1@us.com", senha = "us1"),
    Usuario(id=2, email = "us2@us.com", senha = "us2"),
    Usuario(id=3, email = "us3@us.com", senha = "us3")
]

#GET Retornando os Usuarios
@app.get("/usuarios")

def get_todos_usuarios():
    return base_de_dados

#GET Retorno pelo ID
@app.get("/usuarios/{id_usuario}")

def get_usuario_pelo_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return Usuario

    return {"Status": 404, "Mensagem": "Não encontramos o usuário"}

#POST Inserir usuarios
@app.post("/usuarios")

def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario)
    return usuario
