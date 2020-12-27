import os


def pytest_configure():
    """
    Configuration before any tests
    :return:
    """
    os.environ['MEDIA_ORGANIZER_CONFIG'] = os.path.dirname(os.path.realpath(__file__))
