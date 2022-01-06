import os
import sys

from enum import Enum

BuildingState = Enum('BuildingState', 'FaceDown FaceUp Discarded OutOfGame Wondered Built')

Resource = Enum('Resource', 'Wood Brick Stone Glass Paper')

BuildingType = Enum('BuildingType', 'Red Yellow Green Brown Gray Blue Guild Temple Wonder')

BuildingAge = Enum('BuildingAge', 'One Two Three NoAge')

BuildingOwner = Enum('BuildingOwner', 'P1 P2 NoOne')

ScienceSymbol = Enum('ScienceSymbol', 'Wheel Writing Geometry Medicine Laws Compass Construction')

class Player:
    def __init__(self) -> None:
        pass

class Building:
    def __init__(self, age: BuildingAge, type: BuildingType, costs: list, effects: dict) -> None:
        self.state = BuildingState.FaceUp
        self.owner = BuildingOwner.NoOne
        self.age = age
        self.type = type
        self.effects = effects
        self.covered_by = []
        self.costs = costs
        return

    def can_build(self, inventory):
        return min([cost(inventory) for cost in self.costs])

    def build(self, player: BuildingOwner):
        self.owner = player
        return

class Player:
    def __init__(self, player) -> None:
        self.player = player
        self.inventory = {
            "building": [],
            "dev_token": [],
            "god_token": [],
            "prayer_token": [],
            "science_token": [],
            "gold": 7,
            "points": 0,
            "war": 0,
        }
        return

class DevToken:
    def __init__(self, effects: list) -> None:
        self.effects = effects
        self.owner = BuildingOwner.NoOne
        return

Buildings = {
    # red
    # yellow
    # green
    # brown
    "lumber_camp": Building(age=BuildingAge.One, type=BuildingType.Brown, effects={"produce": [[Resource.Wood]]}),
    # gray
    # blue
    # guild
    # temple
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

DevToken = {
    "agriculture": DevToken(effects={"points": 4, "gold": 6}),
    # their spending goes to you
    "economy": DevToken(effects={}),
    "law": DevToken(effects={"science": ScienceSymbol.Laws}),
}

def main():
    return

if __name__ == "__main__":
    main()