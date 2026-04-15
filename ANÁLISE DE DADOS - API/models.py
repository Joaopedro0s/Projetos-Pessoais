from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Numeric
from decimal import Decimal
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    telefone = Column(String(16), nullable=False)
    endereco = Column(String(100), nullable=False)
    data_cadastro = Column(Date, nullable=False)

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    categoria = Column(String(50), nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    estoque = Column(Integer, nullable=False)

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    data_pedido = Column(Date, nullable=False)
    status = Column(String(50), nullable=False, default="Pendente")

class Itens_Pedido(Base):
    __tablename__ = "itens_pedidos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Numeric(10, 2), nullable=False)