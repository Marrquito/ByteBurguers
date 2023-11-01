from typing import List
from database.models.item_pedido import ItemPedidoDBModel

from database.database import Base
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

class PedidoDBModel(Base):
    __tablename__       = "pedido"

    id                  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mesa_id             : Mapped[int] = mapped_column(ForeignKey("mesa.id"))
    cliente_id          : Mapped[int] = mapped_column(ForeignKey("user.id"))
    date                : Mapped[str] = mapped_column()
    time                : Mapped[str] = mapped_column()
    total               : Mapped[float] = mapped_column()
    item_pedido         : Mapped[List["ItemPedidoDBModel"]] = relationship()

    def __repr__(self) -> str:
        return f"Pedido [id={self.id}, mesa={self.mesa_id}"