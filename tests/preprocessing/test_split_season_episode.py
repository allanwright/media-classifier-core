from mcshared import preprocessing

def test_split_season_episode_standard():
    assert preprocessing.prepare_input('s01e01') == 's01 e01'

def test_split_season_episode_alternate():
    assert preprocessing.prepare_input('01x01') == 's01 e01'