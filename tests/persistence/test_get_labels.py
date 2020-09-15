# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from mccore import prediction

def test_get_labels_not_null():
    assert prediction.get_labels() is not None

def test_labels_has_items():
    assert len(prediction.get_labels()) > 0
