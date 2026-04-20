from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Coordinates(Base):

    __tablename__ = "container_storage"

    cell_id: Mapped[str] = mapped_column(primary_key=True, unique=True)
    layer: Mapped[str] = mapped_column(nullable=False)
    row_num: Mapped[int] = mapped_column(nullable=False) # 1 <= x <= 30
    coord_type: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[str] = mapped_column(default='0')
