import pytest
from mccore import preprocessing

def test_split_season_episode_empty():
    assert preprocessing.prepare_input('') == ''

def test_split_season_episode_invalid():
    assert preprocessing.prepare_input('1234') == '1234'

@pytest.mark.parametrize('input, expected',
    [('s01e01', 's01 e01'),
    ('S01E01', 's01 e01'),
    ('S01e01', 's01 e01'),
    ('s9999e9999', 's9999 e9999')])
def test_split_season_episode_standard_format(input, expected):
    assert preprocessing.prepare_input(input) == expected

""" def test_split_season_episode_std_upper():
    assert preprocessing.prepare_input('S01E01') == 's01 e01'

def test_split_season_episode_std_mixed():
    assert preprocessing.prepare_input('S01e01') == 's01 e01'

def test_split_season_episode_std_large_numbers():
    assert preprocessing.prepare_input('s9999e9999') == 's9999 e9999' """

@pytest.mark.parametrize('input, expected',
    [('01x01', 's01 e01'),
    ('01X01', 's01 e01'),
    ('9999x9999', 's9999 e9999')])
def test_split_season_episode_alternate_format(input, expected):
    assert preprocessing.prepare_input(input) == expected