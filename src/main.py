import os
import sys

from enum import Enum

BuildingState = Enum(
    "BuildingState", "FaceDown FaceUp Discarded OutOfGame Wondered Built"
)

Resource = Enum("Resource", "Wood Brick Stone Glass Paper")

BuildingType = Enum(
    "BuildingType", "Red Yellow Green Brown Gray Blue Guild Temple Wonder"
)

BuildingAge = Enum("BuildingAge", "One Two Three NoAge")

BuildingOwner = Enum("BuildingOwner", "P1 P2 NoOne")

ScienceSymbol = Enum(
    "ScienceSymbol", "Wheel Writing Geometry Medicine Laws Compass Construction"
)


class Player:
    def __init__(self) -> None:
        pass


class Building:
    def __init__(
        self, age: BuildingAge, type: BuildingType, costs: list, effects: dict
    ) -> None:
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
            "coin": 7,
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
    # red - age 1
    "guard_tower": Building(
        age=BuildingAge.One,
        type=BuildingType.Red,
        effects=[{"war": 1}],
    ),
    # red - age 2
    "guard_tower": Building(
        age=BuildingAge.Two,
        type=BuildingType.Red,
        costs=[{Resource.Stone: 2}],
        effects=[{"war": 2}],
    ),
    # yellow - age 1
    "tavern": Building(
        age=BuildingAge.One,
        type=BuildingType.Yellow,
        effects=[{"coin": 4, "chain": "lighthouse"}],
    ),
    # yellow - age 2
    "forum": Building(
        age=BuildingAge.Two,
        type=BuildingType.Yellow,
        costs=[{Resource.Brick: 1, "coin": 3}],
        effects=[{Resource.Glass: 1}, {Resource.Paper: 1}],
    ),
    "caravansery": Building(
        age=BuildingAge.Two,
        type=BuildingType.Yellow,
        costs=[{Resource.Glass: 1, Resource.Paper: 1, "coin": 2}],
        effects=[{Resource.Wood: 1}, {Resource.Stone: 1}, {Resource.Brick: 1}],
    ),
    "customs_house": Building(
        age=BuildingAge.Two,
        type=BuildingType.Yellow,
        costs=[{"coin": 4}],
        effects=[{(Resource.Glass, "coin"): 1, (Resource.Paper, "coin"): 1}],
    ),
    # green
    "workshop": Building(
        age=BuildingAge.One,
        type=BuildingType.Green,
        costs=[{Resource.Paper: 1}],
        effects=[{ScienceSymbol.Geometry: 1, "points": 1}],
    ),
    # brown - age i
    "lumber_yard": Building(
        age=BuildingAge.One,
        type=BuildingType.Brown,
        effects={"produce": [{Resource.Wood: 1}]},
    ),
    "logging_camp": Building(
        age=BuildingAge.One,
        type=BuildingType.Brown,
        costs=[{"coin": 1}],
        effects={"produce": [{Resource.Wood: 1}]},
    ),
    "clay_pool": Building(
        age=BuildingAge.One,
        type=BuildingType.Brown,
        effects={"produce": [{Resource.Brick: 1}]},
    ),
    "clay_pit": Building(
        age=BuildingAge.One,
        type=BuildingType.Brown,
        costs=[{"coin": 1}],
        effects={"produce": [{Resource.Brick: 1}]},
    ),
    "quarry": Building(
        age=BuildingAge.One,
        type=BuildingType.Brown,
        effects={"produce": [{Resource.Stone: 1}]},
    ),
    "stone_pit": Building(
        age=BuildingAge.One,
        type=BuildingType.Brown,
        costs=[{"coin": 1}],
        effects={"produce": [{Resource.Stone: 1}]},
    ),
    # brown - age 2
    "sawmill": Building(
        age=BuildingAge.Two,
        type=BuildingType.Brown,
        costs=[{"coin": 2}],
        effects={"produce": [{Resource.Wood: 2}]},
    ),
    "brickyard": Building(
        age=BuildingAge.Two,
        type=BuildingType.Brown,
        costs=[{"coin": 2}],
        effects={"produce": [{Resource.Brick: 2}]},
    ),
    "shelf_quarry": Building(
        age=BuildingAge.Two,
        type=BuildingType.Brown,
        costs=[{"coin": 2}],
        effects={"produce": [{Resource.Stone: 2}]},
    ),
    # gray - age 1
    "glassworks": Building(
        age=BuildingAge.One,
        type=BuildingType.Gray,
        costs=[{"coin": 1}],
        effects={"produce": [{Resource.Glass: 1}]},
    ),
    "press": Building(
        age=BuildingAge.One,
        type=BuildingType.Gray,
        costs=[{"coin": 1}],
        effects={"produce": [{Resource.Paper: 1}]},
    ),
    # gray - age 2
    "glassblower": Building(
        age=BuildingAge.Two,
        type=BuildingType.Gray,
        effects={"produce": [{Resource.Glass: 1}]},
    ),
    "drying_room": Building(
        age=BuildingAge.Two,
        type=BuildingType.Gray,
        effects={"produce": [{Resource.Paper: 1}]},
    ),
    # blue - age 1
    # blue - age 2
    "tribunal": Building(
        age=BuildingAge.Two,
        type=BuildingType.Blue,
        costs=[{Resource.Wood: 2, Resource.Glass: 1}],
        effects={"points": 5},
    ),
    # guild
    # temple
    # wonders
    "appian_way": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={"points": 3, "coin": 3, "opponent_coin": -3},
    ),
    "circus_maximus": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={"war": 1, "points": 3, "opponent_discard": BuildingType.Gray},
    ),
    "the_colossus": Building(
        age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"war": 2, "points": 3}
    ),
    # todo: the_great_library
    "the_great_lighthouse": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={
            "produce": [
                {
                    Resource.Wood: 1,
                    Resource.Brick: 1,
                    Resource.Stone: 1,
                }
            ],
            "points": 4,
        },
    ),
    "hanging_garden": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={"coin": 6, "points": 3, "carry": True},
    ),
    "the_mausoleum": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={"points": 2, "revive": True},
    ),
    "the_piraeus": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={
            "produce": [{Resource.Glass: 1}, {Resource.Paper: 1}],
            "points": 2,
            "carry": True,
        },
    ),
    "the_pyramids": Building(
        age=BuildingAge.NoAge, type=BuildingType.Wonder, effects={"points": 9}
    ),
    "the_sphinx": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={"points": 6, "carry": True},
    ),
    "the_statue_of_zeus": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={"war": 1, "points": 3, "opponent_discard": BuildingType.Brown},
    ),
    "the_temple_of_artemis": Building(
        age=BuildingAge.NoAge,
        type=BuildingType.Wonder,
        effects={"coin": 12, "carry": True},
    ),
}

DevToken = {
    "agriculture": DevToken(effects={"points": 4, "coin": 6}),
    # their spending goes to you
    "economy": DevToken(effects={}),
    "law": DevToken(effects={"science": ScienceSymbol.Laws}),
    "philosophy": DevToken(effects={"points": 7}),
    "strategy": DevToken(),
    # modifiers for building cost, coin gained, war, carry, points,
}


def main():
    return


if __name__ == "__main__":
    main()
