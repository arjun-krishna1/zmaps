from uuid import UUID
from enum import Enum

from typing import List, Optional
from pydantic import BaseModel

class TypeOfLandmark(str, Enum):
  '''a pre-defined list of possible landmark types'''
  zombie_horde = 'zombie horde'
  resource_stash = 'resource stash'
  outpost = 'outpost'

class LocationOfInterest(BaseModel):
    '''store a location of interest'''
    location: str
    type_of_landmark: TypeOfLandmark

class StageOfDecomposition(int, Enum):
  '''store the average stage of decomposition of the zombie horde'''
  fresh=1
  starting_to_decompose=2
  very_decomposed = 3

class ZombieHorde(BaseModel):
  '''store information about a zombie horde'''
  number_of_zombies: int
  average_stage_of_decomposition: StageOfDecomposition

class WeaponCollection(BaseModel):
  '''store information about a type of weapon, what it is and how many of it there are'''
  type_of_weapon: str
  num_of_weapons: int

class FoodCollection(BaseModel):
  '''store information about a type of food, what it is and how many kilograms of it there are'''
  type_of_food: str
  kilograms_of_food: int

class ResourceStash(BaseModel):
  '''store information about a stash of resources'''
  litres_of_water: int
  litres_of_gasoline: int
  weapon_collections: List[WeaponCollection]
  food_collections: List[FoodCollection]
  technologies: List[str]

class TypeOfOutpost(str, Enum):
  '''a list of types of outpost that an outpost can be'''
  military = 'military'
  civilian = 'civilian'

class Outpost(BaseModel):
  '''store information about an outpost'''
  type_of_outpost: TypeOfOutpost
  size_of_population: int
  resources: ResourceStash
  accepting_survivors: bool
  has_internet: bool