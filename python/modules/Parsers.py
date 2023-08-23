#! /usr/bin/python3

import argparse

class Parsers:
    '''
        Parsing through the arguments to add flexibility to the use of the program
    '''
    # Variables #
    main_parser = None

    def __init__(self):
        self.main_parser = argparse.ArgumentParser(
            description='A wrapper program that allows the user to use the formulea found in the `python_maths` section',
            prog='maths.py'
        )

