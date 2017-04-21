from utils import test_question, LinkedListNode, create_linked_list, reduce_linked_list_to_str


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
