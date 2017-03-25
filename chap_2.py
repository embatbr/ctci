from utils import LinkedListNode, create_linked_list, reduce_linked_list_to_str


def question_1():
    print('##### Remove Dups #####\n')

    # time: O(N); space: O(1)
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

    tests = [('', ''), ('abcdee', 'abcde'), ('abcddefacdlkasdlk', 'abcdeflks'),
             ('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'),
             ('abcdeyzabcd', 'abcdeyz')]

    for test in tests:
        print("version 1 => '{}' becomes '{}': {}".format(test[0], test[1], version_1(test)))
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
        print('version 1 => k = {}, in list {} is {}: {}'.format(test[1], test[0], test[2], version_1(test)))
        print()


def question_3():
    print('##### Delete Middle Node #####\n')
