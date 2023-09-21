from database.database import Base
from sqlalchemy.orm    import Mapped, mapped_column

class UserDBModel(Base):
    __tablename__       = "user"
    
    id                  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name                : Mapped[str]
    last_name           : Mapped[str]
    email               : Mapped[str]
    password            : Mapped[str]
    phone               : Mapped[str]
    
    def __repr__(self) -> str:
        return f"User [name={self.name}, last_name={self.last_name}]"