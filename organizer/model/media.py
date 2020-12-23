import os
import shutil

from organizer.util.arguments import is_option
from organizer.util.file import get_file_target, sizeof_fmt
from organizer.util.logger import logger
from organizer.util.scanner import is_ignored


class Media:

    def __init__(self, file: str):
        self.file = file
        self.ignored = is_ignored(file)
        self.target = None
        self.exists = None
        self.copied = False

        self.process()

    def get_file_size(self, human_readable: bool = True):
        if human_readable:
            return sizeof_fmt(self.get_file_size(False))
        return os.path.getsize(self.file)

    def process(self):
        if self.ignored:
            return
        self.target = get_file_target(self.file)
        self.exists = os.path.exists(self.target)

    def get_filename(self):
        return os.path.basename(self.file)

    def copy_to_target(self):
        if self.ignored or self.exists or self.copied:
            return

        logger.info('Copying media %s to %s -> %s' % (
            self.file,
            self.target,
            self.get_file_size()
        ))

        if not is_option('dry-run'):
            shutil.copy2(self.file, self.target)
        self.copied = True
