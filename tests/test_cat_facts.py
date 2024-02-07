from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_receive_cat_fact():
    mock_requester = Mock()
    mock_response = Mock()
    cat_fact = CatFacts(mock_requester)
    mock_response.json.return_value = {'fact': 'Cats are very cute'}
    mock_requester.get.return_value = mock_response
    assert cat_fact.provide() == 'Cat fact: Cats are very cute'