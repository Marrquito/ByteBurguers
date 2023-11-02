import datetime
from typing             import List

from database.database  import Base
from sqlalchemy         import DateTime, ForeignKey
from sqlalchemy.orm     import Mapped, mapped_column, relationship

class UserDBModel(Base):
    __tablename__       = "user"
    
    id                  : Mapped[int]               = mapped_column(primary_key=True, autoincrement=True)
    name                : Mapped[str]
    last_name           : Mapped[str]
    email               : Mapped[str]
    phone               : Mapped[str]
    city                : Mapped[str]
    watch_on            : Mapped[bool]              = mapped_column(default=False)   
    is_flamengo         : Mapped[bool]              = mapped_column(default=False) 
    orders              : Mapped["OrderDBModel"]    = relationship("OrderDBModel", back_populates="user")

    def __repr__(self) -> str:
        return f"User [name={self.name}, last_name={self.last_name}]"
    
class TableDBModel(Base):
    __tablename__       = "table"

    id               : Mapped[int]              = mapped_column(primary_key=True, autoincrement=True)
    qntd_assentos    : Mapped[int]
    busy             : Mapped[bool]
    orders           : Mapped["OrderDBModel"]   = relationship("OrderDBModel", back_populates="table")

    def __repr__(self) -> str:
        return f"Table [numero={self.id}, status={self.busy}, assentos={self.qntd_assentos}]"
    
class OrderDBModel(Base):
    __tablename__       = "order"

    id                  : Mapped[int]                           = mapped_column(primary_key=True, autoincrement=True)
    time                : Mapped[str]                           = mapped_column(DateTime(timezone=True), default=datetime.datetime.now, onupdate=datetime.datetime.now)
    total               : Mapped[float]
    payment_method      : Mapped[str]
    user_id             : Mapped[int]                           = mapped_column(ForeignKey("user.id"))
    user                : Mapped["UserDBModel"]                 = relationship("UserDBModel", back_populates="orders")
    table_id            : Mapped[int]                           = mapped_column(ForeignKey("table.id"))
    table               : Mapped["TableDBModel"]                = relationship("TableDBModel", back_populates="orders")
    items_ordered       : Mapped[List["ItemOrderedDBModel"]]    = relationship("ItemOrderedDBModel", back_populates="order")
    
    def __repr__(self) -> str:
        return f"Order [id={self.id}, mesa={self.mesa_id}"

class MenuDBModel(Base):
    __tablename__       = "menu"
    
    id                  : Mapped[int]                   = mapped_column(primary_key=True, autoincrement=True)
    name                : Mapped[str]
    description         : Mapped[str]
    fabrication_place   : Mapped[int]
    cost                : Mapped[float]
    item_ordered        : Mapped["ItemOrderedDBModel"]  = relationship("ItemOrderedDBModel", back_populates="menu")
    
    def __repr__(self) -> str:
        return f"Menu [id={self.id}, nome={self.name}]"

class ItemOrderedDBModel(Base):
    __tablename__       = "itemsOrdered"

    id              : Mapped[int]               = mapped_column(primary_key=True, autoincrement=True)
    qtd             : Mapped[int]
    total_price     : Mapped[float]
    order_id        : Mapped[int]               = mapped_column(ForeignKey("order.id"))
    order           : Mapped["OrderDBModel"]    = relationship("OrderDBModel", back_populates="items_ordered")
    menu_id         : Mapped[int]               = mapped_column(ForeignKey("menu.id"))
    menu            : Mapped["MenuDBModel"]     = relationship("MenuDBModel", back_populates="item_ordered")

    def __repr__(self) -> str:
        return f"Table [numero={self.id}, status={self.busy}, assentos={self.qntd_assentos}]"