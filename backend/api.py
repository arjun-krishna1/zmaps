from fastapi import FastAPI
from typing import List, Union

from fastapi.encoders import jsonable_encoder

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


@app.post('/locations/{location}/{type_of_landmark}')
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

@app.get('/locations/{location}')
async def get_location(
    location: str
):
    '''get instance with the coordinates passed in'''
    this_location = None
    for i in locations_of_interest:
        if i.location == location:
            this_location = i
            break

    return this_location

'''
*args -> is used to pass a variable number of arguments
            to a function

**kwargs ->

exclude_unset=True, is for partial updates
generate a dict with only the data was set, omitting default values

'''
def pop_location(
    location: str
    ):

    this_location = None
    for i in range(len(locations_of_interest)):
        location_i = locations_of_interest[i]
        if location_i.location == location:
            this_location = locations_of_interest.pop(i)
            break
    
    return this_location

@app.put('/locations/{location}', response_model=LocationOfInterest)
async def patch_location(
    location: str,
    location_of_interest: LocationOfInterest
):
    '''patch instance with the coordinates passed in 
    and the information passed in'''
    update_item_encoded = jsonable_encoder(location_of_interest)

    for i in range(len(locations_of_interest)):
        if locations_of_interest[i].location == location:
            locations_of_interest.pop(i)
            break

    locations_of_interest.append(update_item_encoded)
    return update_item_encoded

@app.delete('/locations/{location}')
async def delete_location(
    location: str
):
    '''delete instance with the location the same as 
    that is passed in'''
    location_of_interest = None
    for i in range(len(locations_of_interest)):
        if locations_of_interest[i].location == location:
            location_of_interest = locations_of_interest.pop(i)
            break

    return location_of_interest