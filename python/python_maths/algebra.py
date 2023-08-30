#! /usr/bin/python3

import math
import re

from ..modules.Enums import LinearEquationForm

class Identities(object):
    '''
        Formulae that express identities of algebraic functions
    '''

    # Static Methods #
    @staticmethod
    def distance(a: tuple(str,str) | tuple(float,float) | tuple(int,int), b: tuple(str,str) | tuple(float,float) | tuple(int,int), solve: bool=False) -> str | float:
        '''
            Given two points, calculating the distance formula and display either the transformed equation or the solution

            Formula: 
                ab = sqrt((x_b-x_a)^2+(y_b-y_a)^2)
            
            :type a: tuple(str,str) | tuple(float,float) | tuple(int,int)
            :param a: a point to be evaluated

            :type b: tuple(str,str) | tuple(float,float) | tuple(int,int)
            :param b: another point to be evaluated

            :rtype: str | float
            :returns: transformation or solution
        '''
        pass
    
    @staticmethod
    def exponents(expression: str, solve: bool=False) -> str | float:
        '''
            Using the different identities for exponents to display either the transformed equation or the solution
        
            Exponent Identities:
                a^0=1, a!=0
                (a^n)^m = a^(nm)
                (ab)^n = a^nb^n
                a^na^m = a^(n+m)
                a^(-1) = 1/(a^n)
                1/(a^(-n)) = a^n
                a^n + a^m = a^(n+m)
                (a^n)/(a^m) = a^(m-n)
                (a/b)^n = (a^n)/(b^n)
                (a/b)^(-n) = (b/a)^n = (b^n)/(a^n)

            :type expression: str
            :param expression: the expression to be evaluated

            :type solve: bool
            :param solve: display the solution of the function as opposed to just the transformation (default: False)
        
            :rtype: str | float
            :returns: transformation or solution
        '''
        pass

    @staticmethod
    def factoring(expression: str) -> str:
        '''
            Using the different identities of factoring to display either the transformed equation

            Factoring Identities:
                x^2-y^2 = (x-y)(x+y)
                x^3+y^3 = (x+y)(x^2-xy+y^2)
                x^3-y^3 = (x-y)(x^2+xy+y^2)

            :type expression: str
            :param expression: the expression to be evaluated
        
            :rtype: str
            :returns: simplified transformation
        '''
        split:str = None
        # TODO generate Regex
        regex:list = ['','','']
        for i in range(len(regex)):
            value = re.search(pattern=regex[i], string=expression)
            if value != None:
                # TODO make more dynamic
                split = '^2' if i == 0 else '^3'
                break

        assert split != None, f'{expression} does not match the following patterns:\nx^2-y^2\nx^3+y^3\nx^3-y^3'

        vals:list = expression.split(sep=split)[:-1]
        x:str = vals[0]
        y:str = vals[1][1:]
        diff:bool = vals[1][0] == '-'

        if split == '^2':
            solution:str = f'({x} - {y})({x} + {y})'
        elif diff:
            solution:str = f'({x} - {y})({x}^2 + {x}*{y} + {y}^2)'
        else:
            solution:str = f'({x} + {y})({x}^2 - {x}*{y} + {y}^2)'
        
        # TODO simplify

        return solution


    # TODO determine how the expression will be passed in
    @staticmethod
    def linear(form: LinearEquationForm) -> str:
        '''
            Taking the expression and transforming it into the given form

            :type form: LinearEquationForm
            :param form: an enum indicating which form the expression will display as

            :rtype: str
            :returns: the expression of the given form
        '''
        pass

    @staticmethod
    def midpoint(a: tuple(str,str) | tuple(float,float) | tuple(int,int), b: tuple(str,str) | tuple(float,float) | tuple(int,int), solve: bool=False) -> tuple(str,str) | tuple(float,float):
        '''
            Given two points, calculating the midpoint formula and display either the transformed equation or the solution

            Formula: 
                midpoint of bar(ab) = ((x_b+x_a)/2, (y_b+y_a)/2)
            
            :type a: tuple(str,str) | tuple(float,float) | tuple(int,int)
            :param a: a point to be evaluated

            :type b: tuple(str,str) | tuple(float,float) | tuple(int,int)
            :param b: another point to be evaluated

            :rtype: tuple(str,str) | tuple(float)
            :returns: transformation or solution
        '''
        pass

    @staticmethod
    def quadratic(expression: str, solve: bool=False) -> tuple(str,str) | tuple(float,float):
        '''
            Using the quadratic equation to solve for x and displaying either the transformed equation or the solutions

            Formula:
                ax^2+bx+c=0 => x=(-b+sqrt(b^2-4ac))/(2a),(-b-sqrt(b^2-4ac))/(2a)

            If solve is true, the coefficients a,b,c must be values that can be parsed
            
            :type expression: str
            :param expression: the quadratic expression to be evaluated

            :type solve: bool
            :param solve: display the solution of the function as opposed to just the transformation (default: False)

            :rtype: tuple(str,str) | tuple(float,float)
            :returns: transformation or solution
        '''
        # TODO account for if the quadratic expression is missing 'bx' or 'c'
        assert '=' not in expression, f'{expression} must be an expression, not an equation.'

        expression = expression.replace(' ', '')
        a_split:list = expression.split(sep='x^2')
        a:str = a_split[0]

        b_split:list = a_split[1].split(sep='x')
        b_neg:bool = b_split[0][0] == '-'
        b:str = f"{'-' if b_neg else ''}{b_split[0][1:]}"

        c_neg:bool = b_split[1][0] == '-'
        c:str = f"{'-' if c_neg else ''}{b_split[1][1:]}"

        if solve:
            # The following throws a ValueError if it cannot work
            a_num:float = float(a)
            b_num:float = (-1 if b_neg else 1)*float(b)
            c_num:float = (-1 if c_neg else 1)*float(c)
            x_pos:float = (-b_num + math.sqrt(b_num^2 - 4*a_num*c_num)) / (2*a_num)
            x_neg:float = (-b_num + math.sqrt(b_num^2 - 4*a_num*c_num)) / (2*a_num)
        else:
            x_pos:str = f"({'-' if not b_neg else ''}{b} + sqrt(({b})^2 - 4*({a})*({c}))) / (2*({a})"
            x_neg:str = f"({'-' if not b_neg else ''}{b} - sqrt(({b})^2 - 4*({a})*({c}))) / (2*({a})"
        
        return x_pos, x_neg

    @staticmethod
    def slope(a: tuple(str,str) | tuple(float,float) | tuple(int,int), b: tuple(str,str) | tuple(float,float) | tuple(int,int), solve: bool=False) -> str | float:
        '''
            Given two points, calculating the slope formula and display either the transformed equation or the solution

            Formula: 
                m = (y_b - y_a)/(x_b - x_a)
            
            :type a: tuple(str,str) | tuple(float,float) | tuple(int,int)
            :param a: a point to be evaluated

            :type b: tuple(str,str) | tuple(float,float) | tuple(int,int)
            :param b: another point to be evaluated

            :rtype: str | float
            :returns: transformation or solution
        '''
        pass
