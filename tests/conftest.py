import os
import sys

import pytest

from organizer.util.config import BASE_FOLDER, get_config


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    """
    Configuration before any tests
    :return:
    """
    os.environ['MEDIA_ORGANIZER_CONFIG'] = os.path.join(BASE_FOLDER, 'tests')

    print('execution of conftest')

    sys.argv = ['--verbose']
    get_config()
