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


class Item(object):

    def __init__(self, value):
        self.value = value
        self.below = None

class Stack(object):

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value, constructor=Item):
        item = constructor(value)

        if not self.top:
            self.top = item
        else:
            item.below = self.top
            self.top = item

        self.size += 1

    def peek(self):
        if self.top:
            return self.top.value

        return None

    def pop(self):
        if not self.top:
            return None

        value = self.peek()
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

        return array


class ArrayQueue(object):

    def __init__(self):
        self.nodes = list()

    def enqueue(self, node):
        self.nodes.append(node)

    def dequeue(self):
        node = self.nodes[0]
        self.nodes = self.nodes[1 : ]
        return node

    def is_empty(self):
        return not self.nodes

class Node(object):

    def __init__(self, value):
        self.value = value
        self.adjacents = list()
        self.visited = False

    def connect(self, node):
        self.adjacents.append(node)

class Graph(object):

    def __init__(self, nodes, adjacents_list):
        if len(nodes) != len(adjacents_list):
            return Exception('nodes and adjacents_list must have the same length.')

        self.nodes = nodes
        for i in range(len(adjacents_list)):
            node = self.nodes[i]
            adjacents = adjacents_list[i]
            for adjacent in adjacents:
                node.connect(self.nodes[adjacent])

    def flush(self):
        for node in self.nodes:
            node.visited = False

    def dfs(self, source, target):
        source.visited = True

        if source == target:
            return [source.value]
        else:
            for adjacent in source.adjacents:
                if not adjacent.visited:
                    path = self.dfs(adjacent, target)
                    if path:
                        path.insert(0, source.value)
                        return path

        return list()

    def bfs(self, source, target):
        queue = ArrayQueue()

        queue.enqueue(source)

        while not queue.is_empty():
            node = queue.dequeue()

            if node == target:
                return True

            node.visited = True

            for adjacent in node.adjacents:
                if not adjacent.visited:
                    adjacent.visited = True
                    queue.enqueue(adjacent)

        return False
