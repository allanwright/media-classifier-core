# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from mccore import persistence

def test_json_to_obj_null_path_throws_exception():
    with pytest.raises(TypeError):
        persistence.json_to_obj(None)

def test_json_to_obj_empty_path_throws_exception():
    with pytest.raises(FileNotFoundError):
        persistence.json_to_obj('')

def test_json_to_obj_not_null():
    assert persistence.json_to_obj('models/label_dictionary.json') is not None
