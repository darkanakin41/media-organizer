import os

from organizer.__main__ import get_medias, copy_medias_to_target, print_result
from tests.conftest import valid_files


def test_get_medias():
    """
    Test retrieval of medias
    :return:
    """
    medias = get_medias()
    assert len(medias) == len(valid_files()) + 1
    assert len([m for m in medias if not m.ignored]) == len(valid_files())


def test_copy_medias_to_target():
    """
    Test copy of medias
    :return:
    """
    medias = get_medias()
    assert len(medias) == len(valid_files()) + 1
    assert len([m for m in medias if not m.ignored]) == len(valid_files())
    copy_medias_to_target(medias)

    for media in medias:
        if media.copied:
            assert os.path.exists(media.target)
            os.remove(media.target)


def test_display_result():
    """
    Test display result
    :return:
    """
    medias = get_medias()
    assert len(medias) == len(valid_files()) + 1
    assert len([m for m in medias if not m.ignored]) == len(valid_files())
    print_result(medias)
