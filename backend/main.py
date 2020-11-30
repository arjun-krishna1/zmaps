from fastapi import FastAPI
from models import ( 
    LocationOfInterest, TypeOfLandmark
)

home = LocationOfInterest(
    location='Simcoe',
    type_of_landmark=TypeOfLandmark.zombie_horde
    )
app = FastAPI()

@app.get('/')
async def root():
  return {'message': home}