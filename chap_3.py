from utils import StackItem, Stack


def question_2():
    print('##### Stack Min #####\n')

    def version_1(test):
        class StackItemWithMin(StackItem):

            def __init__(self, value):
                super(StackItemWithMin, self).__init__(value)
                self.my_min = value

            def check_min(self):
                if self.below and self.below.my_min < self.my_min:
                    self.my_min = self.below.my_min

        class StackWithMin(Stack):

            def __init__(self):
                super(StackWithMin, self).__init__()

            def push(self, value):
                super(StackWithMin, self).push(value, constructor=StackItemWithMin)
                self.top.check_min()

            def min(self):
                if self.is_empty():
                    return self.top.my_min
                return None

        (given_seq, num_pops, expected) = test

        stack = StackWithMin()

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


def question_3():
    print('##### Stack of Plates #####\n')

    class SetOfStacks(object):

        def __init__(self, threshold):
            self.threshold = threshold
            self.stacks = list()
            self.cur_stack_index = -1;

        def push(self, value):
            if self.cur_stack_index < 0:
                self.stacks.append(Stack())
                self.cur_stack_index = 0

            cur_stack = self.stacks[self.cur_stack_index]

            if cur_stack.size == self.threshold:
                cur_stack = Stack()
                self.stacks.append(cur_stack)
                self.cur_stack_index += 1

            cur_stack.push(value)

        def pop(self):
            if self.cur_stack_index < 0:
                return None

            cur_stack = self.stacks[self.cur_stack_index]

            value = cur_stack.pop()
            if not value:
                return value

            if cur_stack.is_empty():
                self.stacks.remove(cur_stack)
                self.cur_stack_index -= 1

            return value

        def to_array_list(self):
            arrays = list()

            for stack in self.stacks:
                arrays.append(stack.to_array())

            return arrays

    def version_1(test):
        (given_seq, threshold, num_pops, expected) = test

        set_of_stacks = SetOfStacks(threshold)
        for s in given_seq:
            set_of_stacks.push(s)

        for _ in range(num_pops):
            set_of_stacks.pop()

        return set_of_stacks.to_array_list() == expected

    tests = [
        (range(1, 11), 3, 0, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]),
        (range(1, 11), 5, 0, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
        (range(1, 11), 3, 2, [[1, 2, 3], [4, 5, 6], [7, 8]])
    ]

    for test in tests:
        print('version 1 => {} stacked into {} stacks of max size {} and equal to {} after {} pops: {}'.
            format(list(test[0]), len(test[3]), test[1], test[3], test[2], version_1(test)))
        print()
