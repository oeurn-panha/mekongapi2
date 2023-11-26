from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel #data validation
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import desc
import random
from randomnumber import RandNumber

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class RiverData(BaseModel):
    TotDissSens: float
    PHSens: float
    DissOxySens: float
    TempCSens: float
    WaterLevSens: float
    
#==================================================================================================#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()      
#==================================================================================================#
db_dependancy = Annotated[Session, Depends(get_db)]
#==================================================================================================#
stationOne = 1
#==================================================================================================#
# RandNumber.Random()
#==================================================================================================#
@app.post('/riverdata/')
async def Send_River_Data(RiverData: RiverData, db: db_dependancy):
    db_data = models.Data(
        TotDissSens = RiverData.TotDissSens,
        DissOxySens = RiverData.DissOxySens,
        TempCSens = RiverData.TempCSens,
        PHSens = RiverData.PHSens,
        WaterLevSens = RiverData.WaterLevSens,
        Station = stationOne
        )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    
@app.get('/riverdata')
async def Read_River_Data(db:db_dependancy):
    result = db.query(models.Data).order_by(desc(models.Data.id)).first()
    if not result:
        raise HTTPException(status_code=404, detail="database is not found.")
    # ===========================================================#
    db_data = models.Data(
        TotDissSens = random.randrange(1, 400)/4.9,
        DissOxySens = random.randrange(1, 400)/4,
        TempCSens = random.randrange(1, 400)/4,
        PHSens = random.randrange(1, 400)/4,
        WaterLevSens = random.randrange(1, 400)/4,
        Station = stationOne
        )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    # ===========================================================#
    return result
