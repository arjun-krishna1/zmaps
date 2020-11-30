from typing import List
from pydantic import BaseModel, Field

from uuid import UUID, uuid4

# from enums.py
from enums import ( 
  TypeOfLandmark, StageOfDecomposition, TypeOfOutpost )

# best practice, use path variable when specifying a resource
# use query parameters if you want to sort or filter items  
class LocationOfInterest(BaseModel):
    '''store a location of interest'''
    uid: UUID = Field(default_factory=uuid4)
    location: str
    type_of_landmark: TypeOfLandmark

class ZombieHorde(BaseModel):
    '''store information about a zombie horde'''
    uid: UUID = Field(default_factory=uuid4)
    number_of_zombies: int
    average_stage_of_decomposition: StageOfDecomposition


class WeaponCollection(BaseModel):
    '''store information about a type of weapon, what it is and how many of it there are'''
    uid: UUID = Field(default_factory=uuid4)
    type_of_weapon: str
    num_of_weapons: int


class FoodCollection(BaseModel):
    '''store information about a type of food, what it is and how many kilograms of it there are'''
    uid: UUID = Field(default_factory=uuid4)
    type_of_food: str
    kilograms_of_food: int


class ResourceStash(BaseModel):
    '''store information about a stash of resources'''
    uid: UUID = Field(default_factory=uuid4)
    litres_of_water: int
    litres_of_gasoline: int
    weapon_collections: List[WeaponCollection]
    food_collections: List[FoodCollection]
    technologies: List[str]

class Outpost(BaseModel):
    '''store information about an outpost'''
    uid: UUID = Field(default_factory=uuid4)
    type_of_outpost: TypeOfOutpost
    size_of_population: int
    resources: ResourceStash
    accepting_survivors: bool
    has_internet: bool