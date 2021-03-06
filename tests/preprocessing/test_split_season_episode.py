# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from mccore import preprocessing

def test_split_season_episode_empty():
    assert preprocessing.split_season_episode('') == ''

def test_split_season_episode_invalid():
    assert preprocessing.split_season_episode('1234') == '1234'

@pytest.mark.parametrize(
    'name, expected',
    [('s01e01', 's01 e01'),
     ('S01E01', 'S01 E01'),
     ('S01e01', 'S01 e01'),
     ('s9999e9999', 's9999 e9999')])
def test_split_season_episode_standard_format(name, expected):
    assert preprocessing.split_season_episode(name) == expected

@pytest.mark.parametrize(
    'name, expected',
    [('01x01', 's01 e01'),
     ('01X01', 's01 e01'),
     ('9999x9999', 's9999 e9999')])
def test_split_season_episode_x_format(name, expected):
    assert preprocessing.split_season_episode(name) == expected

@pytest.mark.parametrize(
    'name, expected',
    [('s01 ep01', 's01 e01'),
     ('S01 EP01', 's01 e01'),
     ('S9999 Ep9999', 's9999 e9999')])
def test_split_season_episode_ep_format(name, expected):
    assert preprocessing.split_season_episode(name) == expected
