import logging
import sys

from organizer.util.logger import _get_logging_level


def test_get_logging_level_default():
    """
    Test logging level default
    :return:
    """
    sys.argv = []
    assert _get_logging_level() == logging.INFO


def test_get_logging_level_silent():
    """
    Test logging level silent
    :return:
    """
    sys.argv = ['--silent']
    assert _get_logging_level() == logging.ERROR


def test_get_logging_level_verbose():
    """
    Test logging level verbose
    :return:
    """
    sys.argv = ['--verbose']
    assert _get_logging_level() == logging.DEBUG
