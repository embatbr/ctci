from utils import test_question, LinkedListNode, create_linked_list
from utils import reduce_linked_list_to_list, reduce_linked_list_to_str


def question_1():
    print('##### Remove Dups #####\n')

    # time: O(N); space: O(N)
    def version_1(test):
        given = test[0]
        expected = test[1]

        (head, _) = create_linked_list(given) # not considered in the O(.) function calculation

        chars = set()

        if head:
            chars.add(head.value)
            prev = head
            node = head.next
            while node:
                if node.value in chars: # 1st time
                    prev.next = node.next
                else:
                    chars.add(node.value)
                    prev = node

                node = node.next

        output = reduce_linked_list_to_str(head) # not considered in the O(.) function calculation

        return output == expected

    tests = [
        ('', ''),
        ('abcdee', 'abcde'),
        ('abcddefacdlkasdlk', 'abcdeflks'),
        ('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'),
        ('abcdeyzabcd', 'abcdeyz')
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => '{}' becomes '{}'" % version,
                          [test[0], test[1]],
                          locals()['version_%d' % version](test))
        print()


def question_2():
    print('##### Run Kth to Last #####\n')

    # time: O(N); space O(1)
    def version_1(test):
        given = test[0]
        k = test[1]
        expected = test[2]

        (head, _) = create_linked_list(given) # not considered in the O(.) function calculation

        node = head
        num_nodes = 0
        while node:
            num_nodes += 1
            node = node.next

        node = None
        if 0 < k <= num_nodes:
            num_nodes = num_nodes - k
            node = head
            while num_nodes > 0:
                node = node.next
                num_nodes -= 1

            return node.value == expected

        return node == expected

    tests = [
        (list(), 1, None),
        ([1, 2, 3], 3, 1),
        ([1, 2, 3], 0, None),
        ([4, 3, 2, 1], 1, 1),
        ([4, 3, 2, 1], 4, 4),
        ([4, 3, 2, 1], 5, None)
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => k = {}, in list {} is {}" % version,
                          [test[1], test[0], test[2]],
                          locals()['version_%d' % version](test))
        print()


def question_3():
    print('##### Delete Middle Node #####\n')

    # time: O(N); space: O(1)
    def version_1(test):
        given = test[0]
        value = test[1]
        expected = test[2]

        (head, _) = create_linked_list(given) # not considered in the O(.) function calculation

        if head:
            prev = head
            node = head.next
            while node:
                if node.value == value and node.next: # node.next avoids matching the tail
                    prev.next = node.next
                    break

                prev = node
                node = node.next

        output = reduce_linked_list_to_str(head) # not considered in the O(.) function calculation

        return output == expected

    tests = [
        ('', 'a', ''),
        ('abcdef', 'c', 'abdef'),
        ('abcdef', 'a', 'abcdef'),
        ('abcdef', 'f', 'abcdef'),
        ('abbbf', 'b', 'abbf')
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => '{}' after removal of '{}' becomes '{}'" % version,
                          [test[0], test[1], test[2]],
                          locals()['version_%d' % version](test))
        print()


def question_5():
    print('##### Sum Lists #####\n')

    # time: O(N) (where N is the longer input); space O(N)
    def version_1(test):
        (given, expected) = test

        (A, _) = create_linked_list(given[0]) # not considered in the O(.) function calculation
        (B, _) = create_linked_list(given[1]) # not considered in the O(.) function calculation
        carry_on = 0

        head_C = tail_C = None

        while True:
            val_A = A.value if A else 0
            val_B = B.value if B else 0
            result = val_A + val_B + carry_on
            carry_on = 0
            if result > 9:
                result = result - 10
                carry_on = 1

            # has something to insert?
            if result > 0 or carry_on > 0:
                if tail_C:
                    tail_C.next = LinkedListNode(result)
                    tail_C = tail_C.next
                else:
                    head_C = tail_C = LinkedListNode(result)
            else:
                break

            if A:
                A = A.next
            if B:
                B = B.next

        C = reduce_linked_list_to_list(head_C) # not considered in the O(.) function calculation
        return C == expected

    tests = [
        (([7, 1, 6], [5, 9, 2]), [2, 1, 9]),
        (([7, 8, 9], [5, 9, 2]), [2, 8, 2, 1]),
        (([7, 8, 8, 4], [5, 9, 7]), [2, 8, 6, 5])
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => {} + {} = {}" % version,
                          [test[0][0], test[0][1], test[1]],
                          locals()['version_%d' % version](test))
        print()


def question_8():
    print('##### Loop Detection #####\n')

    # time: O(N); space: O(N)
    def version_1(test):
        (given, point, expected) = test

        (head, tail) = create_linked_list(given)

        if point:
            node = head
            cur = 0
            while cur < point:
                node = node.next
                cur += 1

            tail.next = point = node

        # begins here

        visited = set()
        node = head

        while node:
            if node in visited:
                return True == expected

            visited.add(node)
            node = node.next

        return False == expected

    # time: O(N); space: O(1)
    def version_2(test):
        (given, point, expected) = test

        (head, tail) = create_linked_list(given)

        if point:
            node = head
            cur = 0
            while cur < point:
                node = node.next
                cur += 1

            tail.next = point = node

        # begins here

        node_A = node_B = head

        while node_A and node_B:
            if (node_A == node_B) and (node_A != head):
                return True == expected

            node_A = node_A.next
            node_B = node_B.next
            if node_B:
                node_B = node_B.next

        return False == expected

    tests = [
        (['A', 'B', 'C', 'D', 'E', 'F'], None, False),
        (['A', 'B', 'C', 'D', 'E'], 2, True)
    ]

    for test in tests:
        for version in range(1, 3):
            test_question("version %d => {} is {}circular" % version,
                          [test[0], '' if test[2] else 'NOT '],
                          locals()['version_%d' % version](test))
        print()
