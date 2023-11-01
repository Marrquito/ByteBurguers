from typing import List

from database.database import Base
from database.models.pedido import PedidoDBModel
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

class MesaDBModel(Base):
    __tablename__       = "mesa"

    id                  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    qntd_assentos       : Mapped[int] = mapped_column()
    status              : Mapped[bool] = mapped_column()
    pedido              : Mapped[List["PedidoDBModel"]] = relationship()

    def __repr__(self) -> str:
        return f"Mesa [numero={self.id}, status={self.status}, assentos={self.qntd_assentos}]"