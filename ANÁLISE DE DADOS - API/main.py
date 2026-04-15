from fastapi import FastAPI, Depends, HTTPException
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Sistema Loja", \
description="Operações do banco loja_real")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/clientes/", response_model=List[schemas.ClienteResponse])
def listar_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lista = db.query(models.Cliente).offset(skip).limit(limit).all()
    return lista

@app.get("/produtos/", response_model=List[schemas.ProdutoResponse])
def listar_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lista = db.query(models.Produto).offset(skip).limit(limit).all()
    return lista

@app.get("/pedidos/", response_model=List[schemas.PedidoResponse])
def listar_pedidos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lista = db.query(models.Pedido).offset(skip).limit(limit).all()
    return lista

@app.get("/itensPedido/", response_model=List[schemas.ItensPedidosResponse])
def listar_itensPedido(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lista = db.query(models.Itens_Pedido).offset(skip).limit(limit).all()
    return lista