# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from mccore import preprocessing

@pytest.mark.parametrize(
    'name, expected',
    [('a,a,a', 'aaa'),
     (',,a', 'a'),
     ('a,,', 'a')])
def test_prepare_input_removes_commas(name, expected):
    assert preprocessing.prepare_input(name) == expected

def test_prepare_input_outputs_lower():
    assert preprocessing.prepare_input('AbCd') == 'abcd'

@pytest.mark.parametrize(
    'name, expected',
    [('dir/file.ext', 'file ext'),
     ('/dir/file.ext', 'file ext'),
     ('dir1/dir2/file.ext', 'file ext')])
def test_prepare_input_removes_path(name, expected):
    assert preprocessing.prepare_input(name) == expected

def test_prepare_input_normalizes_word_separators():
    assert preprocessing.prepare_input('a.b_c-d[e]f+g') == 'a b c d e f g'

def test_prepare_input_removes_punctuation():
    assert preprocessing.prepare_input(
        '\'\"`~!@#$%^&*()-_+=[]|;:<>,./?{}') == ''

def test_prepare_input_splits_season_episode():
    assert preprocessing.prepare_input('s01e01') == 's01 e01'

@pytest.mark.parametrize(
    'name, expected',
    [(' file.ext', 'file ext'),
     ('file.ext ', 'file ext'),
     ('file  ext', 'file ext'),
     ('file ext', 'file ext')])
def test_prepare_input_removes_extraneous_spaces(name, expected):
    assert preprocessing.prepare_input(name) == expected

@pytest.mark.parametrize(
    'name, expected',
    [('Me & u', 'me and u'),
     ('Me&u', 'me and u'),
     ('Me&', 'me and'),
     ('&u', 'and u')])
def test_prepare_input_converts_ampersand_to_and(name, expected):
    assert preprocessing.prepare_input(name) == expected

def test_prepare_input_movie():
    assert preprocessing.prepare_input(
        'Some.Movie.II (2007).1080p[WEB].mkv') == 'some movie ii 2007 1080p web mkv'

def test_prepare_input_tv():
    assert preprocessing.prepare_input(
        'Some.TV.Show.S01E01.mp4') == 'some tv show s01 e01 mp4'
