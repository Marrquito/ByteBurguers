from database.database import Base
from sqlalchemy.orm    import Mapped, mapped_column

class CardapioDBModel(Base):
    __tablename__       = "cardapio"
    
    id                  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name                : Mapped[str]
    description         : Mapped[str]
    price               : Mapped[float]
    
    def __repr__(self) -> str:
        return f"Cardapio [name={self.name}, last_name={self.last_name}]"