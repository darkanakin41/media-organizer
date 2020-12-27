import os


def array_equals(array1: list, array2: list):
    """
    Check if both contents are the same
    :param array1:
    :param array2:
    :return:
    """
    assert len(array1) == len(array2)
    for val1, val2 in zip(array1, array2):
        assert val1 == val2


def get_test_data_folder():
    """
    Get the test data folder
    :return:
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
