darkanakin41/media-organizer
===

[![integration](https://github.com/darkanakin41/media-organizer/workflows/integration/badge.svg?branch=master)](https://github.com/darkanakin41/media-organizer/actions?query=workflow%3Aintegration)
[![Coverage Status](https://coveralls.io/repos/github/darkanakin41/media-organizer/badge.svg)](https://coveralls.io/github/darkanakin41/media-organizer)

This is a simple way for me to organize my downloaded medias from download folder to the right path.

Based on the configuration, it scan for media files in a folder, retrieve details
from [themoviedb](https://www.themoviedb.org/)
and then copy them to the appropriate target folder.

If the target file already exist, it is not overwrote.

# Usage

First things first, you have to create a configuration file based
on [.media-organizer.yaml.dist](./.media-organizer.yaml.dist).

This file needs to be placed in your home folder or in a path defined in `MEDIA_ORGANIZER_CONFIG` environment variable.

Then you can run the program as described below: 
```shell
$ media-organizer --help
Usage: media-organizer [OPTIONS]

Options:
  --verbose  Verbose mode
  --silent   Silent mode
  --dry-run  Dry Run
  --ignored  Displayed ignored files in results.
  --exists   Displayed target already existing in results.
  --help     Show this message and exit.
```

# Example results :

## When files are copied

```shell
$ media-organizer
[INFO] Retrieve medias and associated datas
[INFO] Processing folder X:\Direct Download
[INFO] Found 4 files
[INFO] Processing folder X:\Torrent\complete
[INFO] Found 130 files
[INFO] Copy medias to target
[INFO] Copying media X:\Direct Download\Saw 2008 TRUEFRENCH MULTI HDLight 1080p-Wawacity vip\Saw.2008.TRUEFRENCH.MULTI.HDLight.1080p-Wawacity.vip.mkv to Y:\Films\French\Saw (2008).mkv -> 2.6 GB
[INFO] Copying media X:\Direct Download\Saw 2009 TRUEFRENCH MULTI HDLight 1080p-Wawacity vip\Saw.2009.TRUEFRENCH.MULTI.HDLight.1080p-Wawacity.vip.mkv to Y:\Films\French\Saw (2009).mkv -> 2.5 GB
[INFO] Copying media X:\Direct Download\Saw 2010 TRUEFRENCH MULTI HDLight 1080p-Wawacity vip\Saw.2010.TRUEFRENCH.MULTI.HDLight.1080p-Wawacity.vip.mkv to Y:\Films\French\Saw (2010).mkv -> 2.4 GB
[INFO] Copying media X:\Direct Download\The Polka King 2017 MULTi 1080p WEB-DL x264-Wawacity vip\The.Polka.King.2017.MULTi.1080p.WEB-DL.x264-Wawacity.vip.mkv to Y:\Films\French\The Polka King (2017).mkv -> 2.1 GB
+----------------------------------------------------------------------------------------------------------------------------+
|                                                            Files                                                           |
+--------------------------------------------------------------+--------+-------------------------------------------+--------+
| File                                                         |   Size | Target                                    | Copied |
+--------------------------------------------------------------+--------+-------------------------------------------+--------+
| Saw.2008.TRUEFRENCH.MULTI.HDLight.1080p-Wawacity.vip.mkv     | 2.6 GB | Y:\Films\French\Saw (2008).mkv            |  True  |
| Saw.2009.TRUEFRENCH.MULTI.HDLight.1080p-Wawacity.vip.mkv     | 2.5 GB | Y:\Films\French\Saw (2009).mkv            |  True  |
| Saw.2010.TRUEFRENCH.MULTI.HDLight.1080p-Wawacity.vip.mkv     | 2.4 GB | Y:\Films\French\Saw (2010).mkv            |  True  |
| The.Polka.King.2017.MULTi.1080p.WEB-DL.x264-Wawacity.vip.mkv | 2.1 GB | Y:\Films\French\The Polka King (2017).mkv |  True  |
+--------------------------------------------------------------+--------+-------------------------------------------+--------+
```

## When nothing have to be done

```shell
$ media-organizer --dry-run
[INFO] Retrieve medias and associated datas
[INFO] Processing folder X:\Direct Download
[INFO] Found 4 files
[INFO] Processing folder X:\Torrent\complete
[INFO] Found 130 files
[INFO] Copy medias to target
[INFO] Nothing to copy, all media are already in the right spot!
```

# TODO

* [ ] Add Unit Testing
* [ ] Add release pipeline

