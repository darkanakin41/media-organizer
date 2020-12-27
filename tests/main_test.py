import os

from organizer import config
from organizer.__main__ import get_medias


def test_get_medias():
    """
    Test retrieval of medias
    :return:
    """
    config['input']['folders'] = [os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'input')]
    config['output'].append({
        'target': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'output'),
        'type': 'movie',
        'filters': {}
    })
    medias = get_medias()
    assert len(medias) == 2
    assert len([m for m in medias if not m.ignored]) == 1
