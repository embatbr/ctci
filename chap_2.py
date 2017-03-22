from utils import LinkedList


def question_1():
    print('##### Remove Dups #####\n')

    # time: O(N); space: O(N)
    def version_1(test):
        given = test[0]
        expected = test[1]

        chars = set()

        output = ''
        for g in given:
            if g not in chars:
                output = '{}{}'.format(output, g)
                chars.add(g)

        return output == expected

    # time: O(N**2); space: O(1)
    def version_2(test):
        given = test[0]
        expected = test[1]

        # this block is not considered in the O(.) function calculation
        head = tail = None
        for g in given:
            node = LinkedList(g)
            if tail:
                tail.next = node
                node.prev = tail
                tail = node
            else:
                head = tail = node

        node_1 = head
        while node_1:
            node_2 = node_1.next
            while node_2:
                if node_1.value == node_2.value:
                    node_2.prev.next = node_2.next
                    if node_2.next:
                        node_2.next.prev = node_2.prev

                node_2 = node_2.next

            node_1 = node_1.next

        # this block is not considered in the O(.) function calculation
        given = ''
        node = head
        while node:
            given = '{}{}'.format(given, node.value)
            node = node.next

        given = ''.join(given)
        return given == expected

    tests = [('', ''), ('abcdee', 'abcde'), ('abcddefacdlkasdlk', 'abcdeflks'),
             ('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz')]

    for test in tests:
        print("version 1 => '{}' becomes '{}': {}".format(test[0], test[1], version_1(test)))
        print("version 2 => '{}' becomes '{}': {}".format(test[0], test[1], version_2(test)))
        print()
