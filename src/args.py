import argparse
import sys

import watchcat

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Watchcat - the simpliest library to watch changes in files")

    parser.add_argument('files', nargs='*', help='''Files for watching.''')

    parser.add_argument('-V', '--verbose', help='''Show which files changed.''')

    args = parser.parse_args()

    if len(sys.argv) < 3:
        print("Please, provide value for -V and at least one file for watching.")
        parser.print_help()
    else:
        w = watchcat.Watchcat(args.verbose, *args.files).run_watching()
        sys.exit(0)
