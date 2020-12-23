import logging
import sys

from organizer.util.arguments import is_option


def _get_logging_level():
    if is_option('silent'):
        return logging.ERROR
    if is_option('verbose'):
        return logging.DEBUG
    return logging.INFO


logger = logging.Logger('app', level=_get_logging_level())
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(_get_logging_level())
handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger.addHandler(handler)
