#!/usr/bin/python3
"""
This module contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    len1 = len(m_a)
    if len1 == 0:
        raise ValueError("m_a can't be empty")
    len2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if len2 is None:
            len2 = len(i)
            if len2 == 0:
                raise ValueError("m_a can't be empty")
        if len2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    l3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if l3 is None:
            l3 = len(i)
            if l3 == 0:
                raise ValueError("m_b can't be empty")
        if l3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(len1):
        l = []
        for j in range(l3):
            n = 0
            for k in range(len2):
                n += m_a[i][k] * m_b[k][j]
            l.append(n)
        matrix.append(l)
    return matrix
