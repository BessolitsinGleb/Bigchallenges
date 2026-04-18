from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Coordinates(Base):

    __tablename__ = "coordinates"

    cell: Mapped[int] = mapped_column(primary_key=True, unique=True)
    layer: Mapped[str] = mapped_column(nullable=False)
    rows: Mapped[int] = mapped_column(nullable=False) # 1 <= x <= 30
    coord_type: Mapped[str] = mapped_column(nullable=False)
    cont_num: Mapped[str] = mapped_column(default='0')
    is_empty: Mapped[bool] = mapped_column(default=False)
