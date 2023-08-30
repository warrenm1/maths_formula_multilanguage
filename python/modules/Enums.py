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
    '''
    ALGEBRA = 'Algebra'
    '''
        A branch of mathematics in which symbols, usually letters of the alphabet, represent numbers or members of a specified set and are used to represent quantities and to express general relationships that hold for all members of the set.
        (definition taken from https://www.wordnik.com/words/algebra)
    '''
    CALCULUS = 'Calculus'
    '''
        The branch of mathematics that deals with limits and the differentiation and integration of functions of one or more variables.
        (definition taken from https://www.wordnik.com/words/calculus)
    '''
    GEOMETRY = 'Geometry'
    '''
        The mathematics of the properties, measurement, and relationships of points, lines, angles, surfaces, and solids.
        (definition taken from https://www.wordnik.com/words/geometry)
    '''
    LINEAR_ALGEBRA = 'Linear Algebra'
    '''
        The branch of mathematics that deals with the theory of systems of linear equations, matrices, vector spaces, determinants, and linear transformations.
        (definition taken from https://www.wordnik.com/words/linear%20algebra)
    '''
    NUMERICAL_SOLUTIONS = 'Numerical Solutions'
    '''
        The study of approximation techniques for solving mathematical problems, taking into account the extent of possible errors.
        (definition taken from https://www.wordnik.com/words/numerical%20analysis)
    '''
    STATISTICS = 'Statistics'
    '''
        The mathematics of the collection, organization, and interpretation of numerical data, especially the analysis of population characteristics by inference from sampling.
        (definition taken from https://www.wordnik.com/words/statistics)
    '''

class LinearEquationForm(EnumExtension):
    '''
        Different Forms of Linear Equations for expressing how to display solutions
    '''
    POINT_SLOPE_FORM = 'Point Slope Form'
    '''
        y - y1 = m(x - x1)
    '''
    SLOPE_INTERCEPT_FORM = 'Slope Intercept Form'
    '''
        Ax + By = C
    '''
    STANDARD_FORM = 'Standard Form'
    '''
        y = mx + b
    '''