from mcshared import preprocessing

def test_prepare_input_removes_commas():
    assert preprocessing.prepare_input('a,a,a') == 'aaa'

def test_prepare_input_removes_leading_commas():
    assert preprocessing.prepare_input(',,a') == 'a'

def test_prepare_input_removes_trailing_commas():
    assert preprocessing.prepare_input('a,,') == 'a'

def test_prepare_input_outputs_lower():
    assert preprocessing.prepare_input('AbCd') == 'abcd'

def test_prepare_input_removes_path():
    assert preprocessing.prepare_input('dir/file.ext') == 'file ext'

def test_prepare_input_removes_path_leading_slash():
    assert preprocessing.prepare_input('/dir/file.ext') == 'file ext'

def test_prepare_input_removes_deep_path():
    assert preprocessing.prepare_input('dir1/dir2/file.ext') == 'file ext'

def test_prepare_input_normalizes_word_separators():
    assert preprocessing.prepare_input('a.b_c-d[e]f+g') == 'a b c d e f g'

def test_prepare_input_removes_punctuation():
    assert preprocessing.prepare_input(
        '\'\"`~!@#$%^&*()-_+=[]|;:<>,./?{}') == ''

def test_prepare_input_splits_season_episode():
    assert preprocessing.prepare_input('s01e01') == 's01 e01'

def test_prepare_input_removes_leading_spaces():
    assert preprocessing.prepare_input(' file.ext') == 'file ext'

def test_prepare_input_removes_trailing_spaces():
    assert preprocessing.prepare_input('file.ext ') == 'file ext'

def test_prepare_input_removes_duplicate_spaces():
    assert preprocessing.prepare_input('file  ext') == 'file ext'

def test_prepare_input_retains_single_spaces():
    assert preprocessing.prepare_input('file ext') == 'file ext'

def test_prepare_input_movie():
    assert preprocessing.prepare_input(
        'Some.Movie.II (2007).1080p[WEB].mkv') == 'some movie ii 2007 1080p web mkv'

def test_prepare_input_tv():
    assert preprocessing.prepare_input(
        'Some.TV.Show.S01E01.mp4') == 'some tv show s01 e01 mp4'