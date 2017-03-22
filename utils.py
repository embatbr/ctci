"""Code useful in many places.
"""


def show_matrix(matrix):
    for line in matrix:
        for elto in line:
            print(elto, end=' ')
        print()


class LinkedList(object):

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
