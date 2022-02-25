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

def test_bld_cost_basic(init_state):
    state = init_state
    assert get_total_coins(state.player1, []) == 0
    assert get_total_coins(state.player1, [{"coin": 4}]) == 4
    assert get_total_coins(state.player1, [{Resource.Wood: 1}]) == 2
    assert get_total_coins(state.player1, [{Resource.Wood: 2, "coin": 2}]) == 6

@pytest.fixture
def p1_p2_has_res():
    tg = TestGame()
    tg.player1.inventory["building"] = [Buildings["lumber_yard"]]
    tg.player2.inventory["building"] = [Buildings["quarry"]]
    return tg

def test_bld_cost_buy(p1_p2_has_res):
    state = p1_p2_has_res
    assert get_total_coins(state.player1, [{Resource.Stone: 1}]) == 3
    assert get_total_coins(state.player1, [{Resource.Wood: 1}]) == 1
    assert get_total_coins(state.player2, [{Resource.Wood: 1, Resource.Brick: 1}]) == 5

@pytest.fixture
def p1_p2_has_optional_chain():
    tg = TestGame()
    tg.player1.inventory["building"] = [Buildings["tavern"], Buildings["glassblower"]]
    tg.player2.inventory["building"] = [Buildings["the_piraeus"]]
    return tg

def test_bld_chain(p1_p2_has_optional_chain):
    state = p1_p2_has_optional_chain
    assert get_total_coins(state.player1, [{"chain": "tavern"}, {"coin": 4}]) == 0
    assert get_total_coins(state.player2, [{"chain": "tavern"}, {"coin": 4}]) == 4

def test_bld_optional(p1_p2_has_optional_chain):
    state = p1_p2_has_optional_chain
    assert get_total_coins(state.player2, [{Resource.Glass: 1}]) == 0
    assert get_total_coins(state.player2, [{Resource.Glass: 1, Resource.Paper: 1}]) == 2
    assert get_total_coins(state.player1, [{Resource.Paper: 1}]) == 2

@pytest.fixture
def p1_p2_has_discount():
    tg = TestGame()
    tg.player1.inventory["building"] = [Buildings["customs_house"]]
    tg.player2.inventory["building"] = [Buildings["quarry"]]
    return tg

def test_bld_buy_at_discount(p1_p2_has_discount):
    state = p1_p2_has_discount
    assert get_total_coins(state.p1, [{Resource.Wood: 1}]) == 1
    assert get_total_coins(state.p1, [{Resource.Wood: 1, Resource.Stone: 1}]) == 2
    assert get_total_coins(state.p1, [{Resource.Wood: 1, Resource.Glass: 1}]) == 3
