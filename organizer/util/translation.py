from organizer.util.logger import logger
from requests.exceptions import HTTPError
from translate import translator

translations = {}


def translate(source, target, phrase) -> str:
    """
    Translate the phrase from the source to the target language
    :param source:
    :param target:
    :param phrase:
    :return:
    """
    if translations.get('%s-%s-%s' % (source, target, phrase)) is not None:
        return translations.get('%s-%s-%s' % (source, target, phrase))
    try:
        translations['%s-%s-%s' % (source, target, phrase)] = translator(source, target, phrase)[0][0][0]
        return translations['%s-%s-%s' % (source, target, phrase)]
    except HTTPError as exce:
        logger.error('Unable to translate the title: %s', exce.args[0])
        translations['%s-%s-%s' % (source, target, phrase)] = ''
        return translations['%s-%s-%s' % (source, target, phrase)]
