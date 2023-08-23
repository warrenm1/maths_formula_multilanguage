#! /usr/bin/python3

from modules import parsers

def main(args):
    pass

if __name__ == '__main__':
    args = parsers.main_parser.parse_args()

    main(args=args)