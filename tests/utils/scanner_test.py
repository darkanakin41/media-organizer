import os

from organizer.util.scanner import scan_folder, is_ignored
from tests.conftest import valid_files
from tests.testutils import get_test_data_folder

data_folder = os.path.join(get_test_data_folder(), 'input')


def test_scan_folder_no_results():
    """
    Test no results
    :return:
    """
    folder = os.path.dirname(os.path.realpath(__file__))
    assert len(scan_folder(folder)) == 0


def test_scan_folder_results():
    """
    Test results
    :return:
    """
    assert len(scan_folder(data_folder)) == len(valid_files()) + 1


def test_is_ignored_true():
    """
    Test no results
    :return:
    """
    file = os.path.join(data_folder, 'test.ignored.mkv')
    assert is_ignored(file)


def test_is_ignored_false():
    """
    Test one result
    :return:
    """
    file = os.path.join(data_folder, 'test.mkv')
    assert not is_ignored(file)
