"""Code useful in many places.
"""


def show_matrix(matrix):
    for line in matrix:
        for elto in line:
            print(elto, end=' ')
        print()
