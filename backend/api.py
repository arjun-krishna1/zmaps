from fastapi import FastAPI
from typing import List, Union

# from models.py
from models import (
    LocationOfInterest, ZombieHorde, WeaponCollection, FoodCollection, ResourceStash, Outpost
)

from enums import (
    TypeOfLandmark, StageOfDecomposition, TypeOfOutpost
)
home = LocationOfInterest(
    location='Simcoe',
    type_of_landmark=TypeOfLandmark.zombie_horde,
    location_info=ZombieHorde(
        number_of_zombies=39,
        average_stage_of_decomposition=StageOfDecomposition.very_decomposed,
    ),
)

# temporary database
locations_of_interest = [home]

# Start API
app = FastAPI()

''''
Query or path parameter?
path parameter when you are working with a single 
  resource (creating, deleting)
query parameter when you are working with many
  resources (returning a list of zombie)
'''


@app.get('/locations')
async def return_locations_of_interest():
    '''return all locations of interest'''
    return {'locations_of_interest': locations_of_interest}


@app.post('/locations/{location}/{type_of_landmark}/')
async def create_location_of_interest(
    location: str, type_of_landmark: TypeOfLandmark,
    location_info: Union[ZombieHorde, Outpost],
):
    '''create a new location of interest'''
    # create a new LocationOfInterest instance
    new_loc = LocationOfInterest(
        location=location,
        type_of_landmark=type_of_landmark,
        location_info=location_info
    )

    # add to temporary database
    locations_of_interest.append(new_loc)

    # return LocationOfInterest instance
    return new_loc
