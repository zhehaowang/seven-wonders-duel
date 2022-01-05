import os
import sys

from enum import Enum

BuildingState = Enum('BuildingState', 'FaceDown FaceUp Discarded OutOfGame Wondered Built')

Resource = Enum('Resource', 'Wood Brick Stone Glass Paper')

BuildingType = Enum('BuildingType', 'Red Yellow Green Brown Gray Blue Guild Temple Wonder')

BuildingAge = Enum('BuildingAge', 'One Two Three NoAge')

BuildingOwner = Enum('BuildingOwner', 'P1 P2 NoOne')

class Player:
    def __init__(self) -> None:
        pass

class Building:
    def __init__(self, age: BuildingAge, type: BuildingType, effects: dict) -> None:
        self.state = BuildingState.FaceUp
        self.owner = BuildingOwner.NoOne
        self.age = age
        self.type = type
        self.effects = effects
        return

Buildings = {
    "lumber_camp": Building(age=BuildingAge.One, type=BuildingType.Brown, effects={"produce": [[Resource.Wood]]}),
    # wonders
    "appian_way": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"points": 3, "gold": 3, "opponent_gold": -3}),
    "circus_maximus": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"war": 1, "points": 3, "opponent_discard": BuildingType.Gray}),
    "the_colossus": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"war": 2, "points": 3}),
    # todo: the_great_library
    "the_great_lighthouse": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"produce": [[Resource.Wood, Resource.Brick, Resource.Stone]], "points": 4}),
    "hanging_garden": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"gold": 6, "points": 3, "carry": True}),
    "the_mausoleum": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"points": 2, "revive": True}),
    "the_piraeus": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"produce": [[Resource.Glass, Resource.Paper]], "points": 2, "carry": True}),
    "the_pyramids": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"points": 9}),
    "the_sphinx": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"points": 6, "carry": True}),
    "the_statue_of_zeus": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"war": 1, "points": 3, "opponent_discard": BuildingType.Brown}),
    "the_temple_of_artemis": Building(age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"gold": 12, "carry": True}),
}

def main():
    return

if __name__ == "__main__":
    main()