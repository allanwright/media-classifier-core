# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest

from mccore.entity_recognizer import EntityRecognizer

@pytest.fixture(name='model')
def fixture_model():
    return EntityRecognizer.load_default()

@pytest.mark.parametrize(
    'name, expected',
    [('Billy Bonka & the Milk Factory (1971) (1080p RedRay x275 16bit Something).mkv',
      'Billy Bonka and the Milk Factory'),
     ('Don\'t.Tell.Dad.The.Garden\'s.Dead.1991.1080p.WEBCut.x275-[YBS.LX].mp4',
      'Don\'t Tell Dad the Garden\'s Dead')])
def test_predict_produces_correct_title(model, name, expected):
    entities = dict(model.predict(name))
    assert entities['title'] == expected
