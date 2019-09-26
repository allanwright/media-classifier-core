import pytest
from mccore import persistence

def test_json_res_to_obj_null_path_throws_exception():
    with pytest.raises(TypeError):
        persistence.json_res_to_obj(None)

def test_json_res_to_obj_empty_path_throws_exception():
    with pytest.raises(IsADirectoryError):
        persistence.json_res_to_obj('')

def test_json_res_to_obj_not_null():
    assert persistence.json_res_to_obj('label_dictionary.json') != None