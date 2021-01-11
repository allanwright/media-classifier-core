# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from mccore import persistence

def test_bin_to_obj_null_path_throws_exception():
    with pytest.raises(TypeError):
        persistence.bin_to_obj(None)

def test_bin_to_obj_empty_path_throws_exception():
    with pytest.raises(FileNotFoundError):
        persistence.bin_to_obj('')

def test_bin_to_obj_not_null():
    assert persistence.bin_to_obj('models/classifier_mdl.pickle') is not None
