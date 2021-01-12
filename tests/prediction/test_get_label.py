# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from mccore import persistence
from mccore import prediction

def test_get_label_null_labels_throws_exception():
    with pytest.raises(TypeError):
        prediction.get_label([0, 1, 0], None)

def test_get_label_returns_int_label_id():
    label, _ = prediction.get_label(
        [0, 1, 0],
        persistence.json_to_obj('models/label_dictionary.json'))
    assert isinstance(label['id'], int)

def test_get_label_returns_string_label_name():
    label, _ = prediction.get_label(
        [0, 1, 0],
        persistence.json_to_obj('models/label_dictionary.json'))
    assert isinstance(label['name'], str)
