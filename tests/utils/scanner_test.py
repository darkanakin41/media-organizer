import os

from organizer.util.scanner import scan_folder


def test_scan_folder_no_results():
    """
    Test no results
    :return:
    """
    folder = os.path.dirname(os.path.realpath(__file__))
    assert len(scan_folder(folder)) == 0


def test_scan_folder_one_result():
    """
    Test one result
    :return:
    """
    folder = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data')
    assert len(scan_folder(folder)) == 1
