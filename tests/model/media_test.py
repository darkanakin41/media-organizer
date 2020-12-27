import os

import pytest

from organizer.model.media import Media
from organizer.util.file import get_file_target
from tests.conftest import valid_files

files = valid_files()

class TestMedia:
    """
    Test media model
    """

    @staticmethod
    @pytest.mark.parametrize("valid_file", files)
    def test_init(valid_file: str):
        """
        Test initialisation
        :param valid_file:
        :return:
        """
        media = Media(valid_file)

        assert media.file == valid_file
        assert media.target == get_file_target(valid_file)
        assert not media.ignored
        assert not media.exists
        assert not media.copied

    @staticmethod
    @pytest.mark.parametrize("valid_file", files)
    def test_get_file_size(valid_file: str):
        """
        Test get_file_size
        :param valid_file:
        :return:
        """
        media = Media(valid_file)

        assert media.get_file_size() == '216.3 KB'
        assert media.get_file_size(human_readable=False) == 221468

    @staticmethod
    @pytest.mark.parametrize("valid_file", files)
    def test_copy_to_target(valid_file: str):
        """
        Test copy to target
        :param valid_file:
        :return:
        """
        media = Media(valid_file)

        media.copy_to_target()

        assert media.copied
        assert os.path.exists(media.target)

        os.remove(media.target)

    @staticmethod
    @pytest.mark.parametrize("valid_file", files)
    def test_copy_to_target_ignored( valid_file: str):
        """
        Test copy to target of an ignored file
        :param valid_file:
        :return:
        """
        media = Media(valid_file)
        media.ignored = True

        media.copy_to_target()

        assert not media.copied
        assert not os.path.exists(media.target)

    @staticmethod
    @pytest.mark.parametrize("valid_file", files)
    def test_filename(valid_file: str):
        """
        Test get filename
        :param valid_file:
        :return:
        """
        media = Media(valid_file)
        assert media.filename == os.path.basename(valid_file)
