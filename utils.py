"""Code useful in many places.
"""


def show_matrix(matrix):
    for line in matrix:
        for elto in line:
            print(elto, end=' ')
        print()


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def create_linked_list(seq, doubly=False):
    head = tail = None
    for s in seq:
        node = LinkedListNode(s)
        if tail:
            tail.next = node
            if doubly:
                node.prev = tail
            tail = node
        else:
            head = tail = node

    return (head, tail)

def reduce_linked_list_to_str(head):
    string = ''

    node = head
    while node:
        string = '{}{}'.format(string, node.value)
        node = node.next

    return string


class StackItem(object):

    def __init__(self, value):
        self.value = value
        self.below = None

class Stack(object):

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value, constructor=StackItem):
        item = constructor(value)

        if not self.top:
            self.top = item
        else:
            item.below = self.top
            self.top = item

        self.size += 1

    def pop(self):
        if not self.top:
            return None

        value = self.top.value
        self.top = self.top.below
        self.size -= 1

        return value

    def is_empty(self):
        return not self.top

    def to_array(self):
        array = list()

        item = self.top
        while item:
            array.append(item.value)
            item = item.below

        array.reverse()

        return array
