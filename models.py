from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, Float
from database import Base

class Data(Base):
    __tablename__ = 'RiverData'
    
    id = Column(Integer, primary_key=True, index=True)
    TotDissSens = Column(Float, index=True)
    DissOxySens = Column(Float, index=True)
    PHSens = Column(Float, index=True)
    TempCSens = Column(Float, index=True)
    WaterLevSens = Column(Float, index=True )
    Station = Column(Integer, index=True)
    