import os

import pytest

from organizer.util.config import get_config


def test_no_config():
    """
    Test with no configuration
    :return:
    """
    old_env = os.environ['MEDIA_ORGANIZER_CONFIG']

    os.environ['MEDIA_ORGANIZER_CONFIG'] = os.path.dirname(os.path.realpath(__file__))

    with pytest.raises(Exception, match=r"No config file found"):
        get_config()

    os.environ['MEDIA_ORGANIZER_CONFIG'] = old_env
