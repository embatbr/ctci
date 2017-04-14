from utils import StackItem, EndlessStack


def question_1():
    print('##### Stack Min #####\n')

    def version_1(test):
        class StackItemWithMin(StackItem):

            def __init__(self, value):
                super(StackItemWithMin, self).__init__(value)
                self.my_min = value

            def check_min(self):
                if self.below and self.below.my_min < self.my_min:
                    self.my_min = self.below.my_min

        class EndlessStackWithMin(EndlessStack):

            def __init__(self):
                super(EndlessStackWithMin, self).__init__()

            def push(self, value):
                super(EndlessStackWithMin, self).push(value, constructor=StackItemWithMin)
                self.top.check_min()

            def min(self):
                if self.top:
                    return self.top.my_min
                return None

        (given_seq, num_pops, expected) = test

        stack = EndlessStackWithMin()

        for s in given_seq:
            stack.push(s)
        for _ in range(num_pops):
            stack.pop()

        print(stack.min())
        return stack.min() == expected

    tests = [
        (list(), 1, None),
        ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], 0, -5),
        ([4, 3, 2, 1, 0, -1, -2, -3, -4, -5], 0, -5),
        ([-2, -3, 4, 0, 3, 1, -1, 2, -4, -5], 1, -4),
        ([-2, -3, 4, 0, 3, 1, -1, 2, -4, -5], 2, -3)
    ]

    for test in tests:
        print("version 1 => {}, after {} pops, min is {}: {}".format(test[0], test[1], test[2], version_1(test)))
        print()
