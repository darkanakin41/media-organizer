import os

from organizer.util.scanner import scan_folder, is_ignored

data_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data')


def test_scan_folder_no_results():
    """
    Test no results
    :return:
    """
    folder = os.path.dirname(os.path.realpath(__file__))
    assert len(scan_folder(folder)) == 0


def test_scan_folder_results():
    """
    Test one result
    :return:
    """
    assert len(scan_folder(data_folder)) == 2


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
