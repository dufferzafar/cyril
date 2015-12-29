#!/usr/bin/env python

"""
Usage: cyril [options] <file>...

Options:
    --all               Do not skip untagged files
    --clean             Remove previously stored lyrics

Example:
    cyril *.mp3
"""

from process import process

from docopt import docopt

__VERSION__ = 0.6


def main():

    args = docopt(
        __doc__,
        version="cyril version %s" % __VERSION__,
        options_first=True,
    )

    for file in args['<file>']:
        process(
            file,
            process_all=args['--all'],
            remove_previous=args['--clean']
        )

if __name__ == '__main__':
    main()
