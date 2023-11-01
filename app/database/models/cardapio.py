from typing import List
#from item_pedido import ItemPedidoDBModel

from database.database import Base
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

class CardapioDBModel(Base):
    __tablename__       = "cardapio"
    
    id                  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name                : Mapped[str]
    description         : Mapped[str]
    price               : Mapped[float]
    item_pedido         : Mapped[List["ItemPedidoDBModel"]] = relationship()
    
    def __repr__(self) -> str:
        return f"Cardapio [id={self.id}, nome={self.name}]"