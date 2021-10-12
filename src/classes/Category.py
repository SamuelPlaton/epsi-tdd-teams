"""
Enum : Category

Description : The enum of our different player weight categories

"""
from enum import Enum

class Category(Enum):
    FLY = 'fly',
    FEATHER = 'feather'
    LIGHT = 'light',
    WELTER = 'welter',
    MEDIUM = 'medium',
    MEDIUM_HEAVY = 'medium_heavy',
    HEAVY = 'heavy',
    SUPER_HEAVY = 'super_heavy',
