from utils import Item, Stack, test_question


def question_2():
    print('##### Stack Min #####\n')

    # time: O(N); space: O(N)
    def version_1(test):
        class ItemWithMin(Item):

            def __init__(self, value):
                super(ItemWithMin, self).__init__(value)
                self.my_min = value

            def check_min(self):
                if self.below and self.below.my_min < self.my_min:
                    self.my_min = self.below.my_min

        class StackWithMin(Stack):

            def __init__(self):
                super(StackWithMin, self).__init__()

            def push(self, value):
                super(StackWithMin, self).push(value, constructor=ItemWithMin)
                self.top.check_min()

            def min(self):
                if self.is_empty():
                    return None

                return self.top.my_min

        (given_seq, num_pops, expected) = test

        stack = StackWithMin()

        for s in given_seq:
            stack.push(s)
        for _ in range(num_pops):
            stack.pop()

        return stack.min() == expected

    tests = [
        (list(), 1, None),
        ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], 0, -5),
        ([4, 3, 2, 1, 0, -1, -2, -3, -4, -5], 0, -5),
        ([-2, -3, 4, 0, 3, 1, -1, 2, -4, -5], 1, -4),
        ([-2, -3, 4, 0, 3, 1, -1, 2, -4, -5], 2, -3)
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => {}, after {} pops, min is {}" % version,
                          [test[0], test[1], test[2]],
                          locals()['version_%d' % version](test))
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

            if cur_stack.is_empty():
                self.stacks.remove(cur_stack)
                self.cur_stack_index -= 1

            return value

        def to_array_list(self):
            arrays = list()

            for stack in self.stacks:
                arrays.append(stack.to_array())

            return arrays

    # time: O(?); space: O(N)
    def version_1(test):
        (given_seq, threshold, num_pops, expected) = test

        set_of_stacks = SetOfStacks(threshold)
        for s in given_seq:
            set_of_stacks.push(s)

        for _ in range(num_pops):
            set_of_stacks.pop()

        return set_of_stacks.to_array_list() == expected

    tests = [
        (range(1, 11), 3, 0, [[3, 2, 1], [6, 5, 4], [9, 8, 7], [10]]),
        (range(1, 11), 5, 0, [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6]]),
        (range(1, 11), 3, 2, [[3, 2, 1], [6, 5, 4], [8, 7]])
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => {} stacked into {} stacks of max size {} and equal to {} after {} pops" % version,
                          [list(test[0]), len(test[3]), test[1], test[3], test[2]],
                          locals()['version_%d' % version](test))
        print()


def question_4():
    print('##### Queue via Stacks #####\n')

    # time: O(N); space: O(N)
    def version_1(test):
        forward_stack = Stack()
        backward_stack = Stack()

        for t in test:
            forward_stack.push(t)

        while not forward_stack.is_empty():
            backward_stack.push(forward_stack.pop())

        result = ''.join(backward_stack.to_array())

        return test == result

    tests = [
        '',
        'abcdefghijklmnopqrstuvwxyz',
        'abcdefghijklmnopqrstuvwxyza',
        'aabbcc',
        'mdifnafanfa',
        'aifasoid',
        'zyxvwutsrqponmlkjihgfedcba'
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => '{}' inserted in queue" % version,
                          [test],
                          locals()['version_%d' % version](test))
        print()


def question_5():
    print('##### Sort Stack #####\n')
    # just use insertion sort

    # time: O(N^2); space: O(N)
    def version_1(test):
        (given, expected) = test

        original_stack = Stack()
        sorted_stack = Stack()

        for g in given:
            original_stack.push(g)

        # starts here

        while not original_stack.is_empty():
            pivot = original_stack.pop()

            while (not sorted_stack.is_empty()) and (pivot < sorted_stack.peek()):
                original_stack.push(sorted_stack.pop())
            sorted_stack.push(pivot)

        # sorts in reverse order (smallest on top)
        while not sorted_stack.is_empty():
            original_stack.push(sorted_stack.pop())

        given_str = ''.join(original_stack.to_array()) # doesn't count in the O(.) calculation
        return given_str == expected

    # time: O(N^2); space: O(N)
    def version_2(test):
        (given, expected) = test

        original_stack = Stack()
        sorted_stack = Stack()

        for g in given:
            original_stack.push(g)

        # starts here

        num_eltos = original_stack.size

        for i in range(num_eltos):
            pivot = original_stack.pop()

            num_swaps = 0
            while (not sorted_stack.is_empty()) and (pivot < sorted_stack.peek()):
                original_stack.push(sorted_stack.pop())
                num_swaps += 1
            sorted_stack.push(pivot)

            for _ in range(num_swaps):
                sorted_stack.push(original_stack.pop())

        # sorts in reverse order (smallest on top)
        while not sorted_stack.is_empty():
            original_stack.push(sorted_stack.pop())

        given_str = ''.join(original_stack.to_array()) # doesn't count in the O(.) calculation
        return given_str == expected

    tests = [
        ('', ''),
        ('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'),
        ('zyxvwutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz'),
        ('wqhrgacdzbmsnlvukjfpteixoy', 'abcdefghijklmnopqrstuvwxyz')
    ]

    for test in tests:
        for version in range(1, 3):
            test_question("version %d => '{}' sorted as '{}'" % version,
                          [test[0], test[1]],
                          locals()['version_%d' % version](test))
        print()
