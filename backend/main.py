from fastapi import FastAPI
from models import ( 
    LocationOfInterest, TypeOfLandmarkEnum
)

home = LocationOfInterest(
    location='Simcoe',
    type_of_landmark=TypeOfLandmarkEnum.zombie_horde
    )
app = FastAPI()

@app.get('/')
async def root():
  return {'message': home}