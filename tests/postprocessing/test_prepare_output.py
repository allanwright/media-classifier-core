import pytest
from mccore import postprocessing

@pytest.mark.parametrize('input, expected',
    [('a,a,a', 'aaa'), (',,a', 'a'), ('a,,', 'a')])
def test_prepare_output_removes_commas(input, expected):
    assert postprocessing.prepare_output(input) == expected

def test_prepare_output_outputs_retains_case():
    assert postprocessing.prepare_output('AbCd') == 'AbCd'

@pytest.mark.parametrize('input, expected',
    [('dir/file.ext', 'file ext'),
    ('/dir/file.ext', 'file ext'),
    ('dir1/dir2/file.ext', 'file ext')])
def test_prepare_output_removes_path(input, expected):
    assert postprocessing.prepare_output(input) == expected

def test_prepare_output_normalizes_word_separators():
    assert postprocessing.prepare_output('a.b_c-d[e]f+g') == 'a b c d e f g'

def test_prepare_output_removes_non_word_characters():
    assert postprocessing.prepare_output(
        '\"`~#^*()-_+=[]|;:<>,./{}') == ''

def test_prepare_output_retains_punctuation():
    assert postprocessing.prepare_output(
        '\'!@$%&?') == '\'!@$%&?'

def test_prepare_output_splits_season_episode():
    assert postprocessing.prepare_output('s01e01') == 's01 e01'

@pytest.mark.parametrize('input, expected',
    [(' file.ext', 'file ext'),
    ('file.ext ', 'file ext'),
    ('file  ext', 'file ext'),
    ('file ext', 'file ext')])
def test_prepare_output_removes_extraneous_spaces(input, expected):
    assert postprocessing.prepare_output(input) == expected

def test_prepare_output_movie():
    assert postprocessing.prepare_output(
        'Some.Movie.II (2007).1080p[WEB].mkv') == 'Some Movie II 2007 1080p WEB mkv'

def test_prepare_output_tv():
    assert postprocessing.prepare_output(
        'Some.TV.Show.S01E01.mp4') == 'Some TV Show S01 E01 mp4'