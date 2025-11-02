from sqlalchemy import Column, Integer, String, DateTime
from config.database import Base

class Menu(Base):
    __tablename__ = "menu"

    id_menu = Column(Integer, primary_key=True, index=True)
    name = Column(String (40), nullable=False)     # misal watt
    price = Column(String(50), nullable=False) # misal "12:30"
    category = Column(String (45), nullable=False) # format datetime
    image_url= Column(String (50), nullable=False) # format datetime

