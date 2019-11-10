from .builder import Builder
import argparse


def main():
    # Start parsing
    parser = argparse.ArgumentParser(prog='dirtree', description='Generates \
                                     a forest tree for a directory.')
    parser.add_argument('dir')
    parser.add_argument('--output', '-o',
                        help='Output to a file instead of the console')
    parser.add_argument('--root', nargs='?', default='',
                        help='Sets the label of the root of the tree')
    parser.add_argument('--ignore', nargs='*', default=[],
                        help='Directories to ignore')
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='Enable logging to console')
    args = parser.parse_args()

    # Start processing
    VERBOSE = args.verbose
    START_PATH = args.dir
    ROOT_NAME = args.root
    IGNORE_DIRS = args.ignore
    OUTPUT_FILE = args.output

    if(VERBOSE):
        print("Verbose mode enabled.")
        print("Start path:", START_PATH)
        print("Label for root node:", ROOT_NAME)
        print("Directories to ignore:", IGNORE_DIRS)

        if OUTPUT_FILE:
            print("Writing output to file:", OUTPUT_FILE)
        else:
            print("Writing output to stdio")

        print()

    b = Builder()
    tree = b.buildRecursive(START_PATH, ROOT_NAME, IGNORE_DIRS)

    if OUTPUT_FILE:
        f = open(OUTPUT_FILE, "w")
        f.write(tree)
    else:
        print(tree)


if __name__ == "__main__":
    main()
