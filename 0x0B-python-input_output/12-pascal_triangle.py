#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    row = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(triangle[-1][j:j+2]))
        triangle.append(row)
    return triangle
