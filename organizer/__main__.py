import sys
from typing import List

import click
from organizer import config
from organizer.model.media import Media
from organizer.util.arguments import is_option
from organizer.util.logger import logger
from organizer.util.scanner import scan_folder
from prettytable import PrettyTable


def print_result(medias: List[Media]):
    headers = ['File', 'Size', 'Target', 'Copied']

    if is_option('ignored'):
        headers.append('Ignored')

    if is_option('exists'):
        headers.append('Exists')

    table = PrettyTable(headers)
    table.align["File"] = "l"
    table.align["Size"] = "r"
    table.align["Target"] = "l"
    table.align["Exists"] = "c"
    table.align["Ignored"] = "c"
    table.align["Copied"] = "c"

    display = False

    for media in medias:
        if (is_option('ignored') or not media.ignored) and (is_option('exists') or not media.exists):
            row = [media.get_filename(), media.get_file_size(), media.target, media.copied]

            if is_option('ignored'):
                row.append(media.ignored)
            if is_option('exists'):
                row.append(media.exists)

            table.add_row(row)

            display = True

    table.title = 'Files'

    if display:
        print(table)
    else:
        logger.info('Nothing to copy, all media are already in the right spot!')


def get_medias():
    files = []
    for folder in config.get('input').get('folders'):
        files += scan_folder(folder)
    files.sort()

    medias = []

    for index, f in enumerate(files):
        logger.debug('Convert to media %d/%d: %s' % (index + 1, len(files), f))
        medias.append(Media(f))

    return medias


def copy_medias_to_target(medias: List[Media]):
    for index, media in enumerate(medias):
        logger.debug('Processing media %d/%d: %s --> %s' % (
            index + 1,
            len(medias),
            media.file,
            media.target,
        ))
        media.copy_to_target()


@click.command()
@click.option('--verbose', is_flag=True, default=False, help='Verbose mode')
@click.option('--silent', is_flag=True, default=False, help='Silent mode')
@click.option('--dry-run', is_flag=True, default=False, help='Dry Run')
@click.option('--ignored', is_flag=True, default=False, help='Displayed ignored files in results.')
@click.option('--exists', is_flag=True, default=False, help='Displayed target already existing in results.')
def main(verbose: bool, silent: bool, dry_run: bool, ignored: bool, exists: bool):
    logger.info('Retrieve medias and associated datas')
    medias = get_medias()
    logger.info('Copy medias to target')
    copy_medias_to_target(medias)
    print_result(medias)


if __name__ == '__main__':
    main()
