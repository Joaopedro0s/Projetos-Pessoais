from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from typing import List

class ClienteBase(BaseModel):
    nome: str
    email: Optional[str] = None
    telefone: str
    endereco: str
    data_cadastro: datetime

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True

class ProdutoBase(BaseModel):
    nome : str
    categoria: str
    preco: float
    estoque: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True

class PedidoBase(BaseModel):
    cliente_id: int
    data_pedido: datetime
    status: str

class PedidoCreate(PedidoBase):
    pass

class PedidoResponse(PedidoBase):
    id: int

    class Config:
        from_attributes = True

class ItensPedidosBase(BaseModel):
    pedido_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float

class ItensPedidosCreate(ItensPedidosBase):
    pass

class ItensPedidosResponse(ItensPedidosBase):
    id: int

    class Config:
        from_attributes = True