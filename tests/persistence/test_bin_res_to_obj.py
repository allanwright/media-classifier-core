import pytest
from mccore import persistence

def test_bin_res_to_obj_null_path_throws_exception():
    with pytest.raises(TypeError):
        persistence.bin_res_to_obj(None)

def test_bin_res_to_obj_empty_path_throws_exception():
    with pytest.raises(IsADirectoryError):
        persistence.bin_res_to_obj('')

def test_bin_res_to_obj_not_null():
    assert persistence.bin_res_to_obj('classifier_mdl.pickle') is not None