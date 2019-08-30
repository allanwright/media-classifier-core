from mcshared import preprocessing

def test_split_season_episode_empty():
    assert preprocessing.prepare_input('') == ''

def test_split_season_episode_invalid():
    assert preprocessing.prepare_input('1234') == '1234'

def test_split_season_episode_std_lower():
    assert preprocessing.prepare_input('s01e01') == 's01 e01'

def test_split_season_episode_std_upper():
    assert preprocessing.prepare_input('S01E01') == 's01 e01'

def test_split_season_episode_std_mixed():
    assert preprocessing.prepare_input('S01e01') == 's01 e01'

def test_split_season_episode_std_large_numbers():
    assert preprocessing.prepare_input('s9999e9999') == 's9999 e9999'

def test_split_season_episode_alt_lower():
    assert preprocessing.prepare_input('01x01') == 's01 e01'

def test_split_season_episode_alt_upper():
    assert preprocessing.prepare_input('01X01') == 's01 e01'

def test_split_season_episode_alt_large_numbers():
    assert preprocessing.prepare_input('9999x9999') == 's9999 e9999'