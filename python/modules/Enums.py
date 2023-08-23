#! /usr/bin/python3

from enum import Enum

# Taken from https://stackoverflow.com/a/54919285/14765680
class EnumExtension(Enum):
    '''
        Wrapper class shared by all of the following enums
    '''
    # Class Method #
    @classmethod
    def raiseAssertError(cls, variable: str):
        '''
            Raises error if an Enum Variable is not of the needed type

            :type variable: str
            :param variable: variable name that isn't the right type
        '''
        raise AssertionError(f'`{variable}` must be an {cls}.')

    @classmethod
    def toList(cls) -> list:
        '''
            Displays the Enum as an array of the values

            :rtype: list
            :returns: list of all the values in the Enum
        '''
        return list(map(lambda c: c.value, cls))
    
    # Static Method #
    @staticmethod
    def switch(statement: map, key) -> str:
        '''
            Simple Switch Statement
            Wrapper around a map to ensure all the associated maps have the needed implementation

            :type statement: map
            :param statement: Map of specific values needed

            :type key: Any
            :param key: keyname for the map

            :rtype: str
            :returns: value in the map
        '''
        string = statement.get(key)
        if string is None:
            raise ValueError(f'Missing implementation of {key} in {statement}')
        return string
    
class MathOptions(EnumExtension):
    '''
        Options for maths the argument

        Enum.name => value
        Enum.value => type
    '''
    ALGEBRA = 'Algebra'
    CALCULUS = 'Calculus'
    GEOMETRY = 'Geometry'
    LINEAR_ALGEBRA = 'Linear Algebra'
    NUMERICAL_SOLUTIONS = 'Numerical Solutions'
    STATISTICS = 'Statistics'