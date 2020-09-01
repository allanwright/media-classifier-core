# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest

from mccore.entity_recognizer import EntityRecognizer

@pytest.fixture
def model():
    return EntityRecognizer.load_default()

@pytest.mark.parametrize(
    'input, expected',
    [('Billy Bonka & the Milk Factory (1971) (1080p RedRay x275 16bit Something).mkv',
      'Billy Bonka and the Milk Factory'),
     ('Don\'t.Tell.Dad.The.Garden\'s.Dead.1991.1080p.WEBCut.x275-[YBS.LX].mp4',
      'Don\'t Tell Dad the Garden\'s Dead')])
def test_predict_produces_correct_title(model, input, expected):
    entities = dict(model.predict(input))
    assert entities['title'] == expected
