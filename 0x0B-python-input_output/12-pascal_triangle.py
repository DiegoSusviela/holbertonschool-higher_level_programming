#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    line = []
    for i in range(n):
        line = [1]
        if i > 0:
            for j in range(i):
                line.append(sum(triangle[-1][j:j+2]))
        triangle.append(line)
    return triangle
