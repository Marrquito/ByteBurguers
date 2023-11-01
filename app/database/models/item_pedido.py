from typing import List

from database.database import Base
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

class ItemPedidoDBModel(Base):
    __tablename__       = "item_pedido"

    id_pedido           : Mapped[int] = mapped_column(ForeignKey("pedido.id"), primary_key=True)
    id_cardapio         : Mapped[int] = mapped_column(ForeignKey("cardapio.id"), primary_key=True)

    def __repr__(self) -> str:
        return f"ItemPedido [id_pedido={self.id_pedido}, id_cardapio={self.id_cardapio}]"