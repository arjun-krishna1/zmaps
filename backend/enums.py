from enum import Enum

class TypeOfLandmark(str, Enum):
    '''a pre-defined list of possible landmark types'''
    zombie_horde = 'zombie horde'
    resource_stash = 'resource stash'
    outpost = 'outpost' 

class StageOfDecomposition(int, Enum):
    '''store the average stage of decomposition of the zombie horde'''
    fresh = 1
    starting_to_decompose = 2
    very_decomposed = 3

class TypeOfOutpost(str, Enum):
    '''a list of types of outpost that an outpost can be'''
    military = 'military'
    civilian = 'civilian'