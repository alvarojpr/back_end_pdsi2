from fastapi import FastAPI, status, Depends
import classes, model
from database import engine, get_db
from sqlalchemy.orm import Session
import requests
from bs4 import BeautifulSoup

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World!"}

@app.post("/criar", status_code=status.HTTP_201_CREATED)
def criar_valores(nova_mensagem: classes.Mensagem, db: Session = Depends(get_db)):
    # mensagem_criada = model.Model_Mensagem(titulo=nova_mensagem.tutulo,conteudo=nova_mensagem.conteudo, publicada=nova_mensagem.publicada)
    mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada)
    return{"Mensagem:": mensagem_criada}

    # print(nova_mensagem)
    # return {"Mensagem": f"Titulo: {nova_mensagem.titulo} Conteudo: {nova_mensagem.conteudo} Publicada: {nova_mensagem.publicada}"}

@app.get("/quadrado/{num}")
def square(num: int):
    return num ** 3

# uvicorn app.main:app --reload --root-path server

# ATUALIZAR
# git fetch origin
# git pull origin main

# SUBIR MUDANÇAS
# git add .                 git add requirements.txt
# git commit -m "mensagem"
# git push origin main

# GERAR E INSATALAR requirements.txt
# pip freeze > requirements.txt
# pip install -r requirements.txt