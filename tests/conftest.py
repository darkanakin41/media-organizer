import os
from typing import List

import pytest

from tests.testutils import get_test_data_folder


def pytest_configure():
    """
    Configuration before any tests
    :return:
    """
    os.environ['MEDIA_ORGANIZER_CONFIG'] = os.path.dirname(os.path.realpath(__file__))
    from organizer import config  # pylint: disable=import-outside-toplevel

    config['input']['folders'] = [os.path.join(get_test_data_folder(), 'input')]
    config['output'].append({
        'target': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'output', 'movie'),
        'type': 'movie',
        'filters': {}
    })
    config['output'].append({
        'target': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'output', 'episode'),
        'type': 'episode',
        'filters': {}
    })
    config['output'].append({
        'target': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'output', 'manga'),
        'type': 'episode',
        'filters': {
            'genres': '(Animation)',
            'original_language': '(ja)'
        }
    })
    config['output'].append({
        'target': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'output', 'other_tv'),
        'type': 'episode',
        'filters': {
            'genres': '(Animation)',
            'original_language': '(en)'
        }
    })


@pytest.fixture
def valid_movie_file() -> str:
    """
    Fixture get a valid movie file
    :return:
    """
    return os.path.join(get_test_data_folder(),
                        'input',
                        'Coherence (2013) VOSTFR AC3 BluRay 1080p x264-[BenH4].mkv')


@pytest.fixture
def valid_tv_file() -> str:
    """
    Fixture get a valid tv file
    :return:
    """
    return os.path.join(get_test_data_folder(),
                        'input',
                        'The IT Crowd S01E01 - Yesterday\'s Jam.mkv')


@pytest.fixture
def valid_manga_file() -> str:
    """
    Fixture get a valid tv file
    :return:
    """
    return os.path.join(get_test_data_folder(),
                        'input',
                        'Assault Lily BOUQUET - s01e01.mkv')


def valid_files() -> List[str]:
    """
    Fixture get valid files
    :return:
    """
    return [os.path.join(get_test_data_folder(),
                         'input',
                         'Coherence (2013) VOSTFR AC3 BluRay 1080p x264-[BenH4].mkv'),
            os.path.join(get_test_data_folder(),
                         'input',
                         'The IT Crowd S01E01 - Yesterday\'s Jam.mkv'),
            os.path.join(get_test_data_folder(),
                         'input',
                         'Assault Lily BOUQUET - s01e01.mkv'),
            ]
