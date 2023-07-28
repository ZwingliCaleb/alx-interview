#!/usr/bin/python3
"""
   Pascal's triangle function
"""


def pascal_triangle(n):
   """returns Pascal's triangle in a list of list"""
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        next_row = [1]

        for j in range(1, i):
            next_row.append(prev_row[j - 1] + prev_row[j])

        next_row.append(1)
        triangle.append(next_row)

    return triangle

