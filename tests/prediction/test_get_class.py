# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from mccore import persistence
from mccore import prediction

@pytest.fixture(name='labels')
def fixture_labels():
    return persistence.json_to_obj('models/label_dictionary.json')

def test_get_class_null_labels_throws_exception():
    with pytest.raises(TypeError):
        prediction.get_class([0, 1, 0], None)

def test_get_class_has_label(labels):
    result = prediction.get_class([0, 1, 0], labels)
    assert 'label' in result

def test_get_class_has_label_id(labels):
    result = prediction.get_class([0, 1, 0], labels)
    assert 'id' in result['label']

def test_get_class_has_label_name(labels):
    result = prediction.get_class([0, 1, 0], labels)
    assert 'name' in result['label']

def test_get_class_has_probability(labels):
    result = prediction.get_class([0, 1, 0], labels)
    assert 'probability' in result

def test_get_class_has_int_label_id(labels):
    result = prediction.get_class([0, 1, 0], labels)
    assert isinstance(result['label']['id'], int)

def test_get_class_has_string_label_name(labels):
    result = prediction.get_class([0, 1, 0], labels)
    assert isinstance(result['label']['name'], str)

def test_get_class_has_float_probability(labels):
    result = prediction.get_class([0, 1, 0], labels)
    assert isinstance(result['probability'], float)
