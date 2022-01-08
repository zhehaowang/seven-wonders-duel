#!/usr/bin/env python3
# python3 -m pytest

from main import *
import pytest

class TestGame:
    def __init__(self):
        self.player1 = Player(BuildingOwner.P1)
        self.player2 = Player(BuildingOwner.P2)

@pytest.fixture
def init_state():
    return TestGame()

def test_bld_cost(init_state):
    assert get_total_coins(init_state.player1, []) == 0
