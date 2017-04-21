from utils import mergesort


def question_1():

    tests = [
        [6, 3, 1, 7, 2, 8, 9, 4],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1]
    ]

    for test in tests:
        print(test)
        mergesort(test)
        print(test)
        print()
