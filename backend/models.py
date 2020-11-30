from enum import Enum

from typing import List, Optional
from pydantic import BaseModel

TYPE_OF_LANDMARKS = ['zombie horde', 'resource stash', 'outpost',]

class TypeOfLandmarkEnum(str, Enum):
  ''' Type of Landmar must be one of these'''
  zombie_horde = 'zombie horde'
  resource_stash = 'resource stash'
  outpost = 'outpost'

class LocationOfInterest(BaseModel):
    location: str
    type_of_landmark: TypeOfLandmarkEnum

'''
  - Zombie horde:
    - Number of zombies
    - Average stage of decomposition
  - Resource stash:
    - Litres of water : int
    - Litres of gasoline : int
    - Weapons : (string, int)
    - Food : (string, int)
    - Technology : string
  - Outpost:
    - Type: Military, Civilian
    - Population size: int
    - Resources : Resource stash
    - Accepting survivors: Boolean
    - Has Internet Access: Boolean
'''