#! /usr/bin/python3

class Vector(object):
    '''
        Formula for manipulations with matrices
    '''

    # Static Methods #
    @staticmethod
    def dotProduct(A: list, B: list) -> int | float:
        '''
            A scalar product of two arrays. 
            i.e. [a1, a2, ..., an]*[b1, b2, ..., bn] = a1*b1 + a2*b2 + ... + an*bn

            Raises an error if the relationship in sizes of A and B are not nx1, where n∈Z+

            :type A: list
            :param A: array of numbers to be multiplied

            :type B: list
            :param B: array of numbers to be multiplied

            :rtype: int | float
            :returns: the dot product of the two arrays
        '''
        assert len(A) == len(B), f'Both arrays in the dot product must be of size nx1, where n∈Z+'

        sum = 0
        for i in len(A):
            sum += A[i]*B[i]
        
        return sum
    