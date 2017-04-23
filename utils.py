"""Code useful in many places.
"""


# ### METACODE ###


def describe_test(description, args):
    return description.format(*args)

def check_test(outcome):
    if outcome == True:
        return 'SUCCESS'
    elif outcome == False:
        return 'FAIL'

    raise Exception("'outcome' must be a boolean.")

def test_question(description, args, outcome):
    print('{}: {}'.format(describe_test(description, args), check_test(outcome)))


def show_matrix(matrix):
    ret = ''

    for line in matrix:
        for elto in line:
            ret = '{}{} '.format(ret, elto)
        ret = '{}\n '.format(ret)

    return ret


# ### LISTS, STACKS AND QUEUES ###


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

def reduce_linked_list_to_list(head):
    ret = list()

    node = head
    while node:
        ret.append(node.value)
        node = node.next

    return ret

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


# ### SORTS ###


def _sorting_loop(array, size, forward=True):
    swapped = False
    iterator = range(size - 1) if forward else range(size - 2, -1, -1)

    for i in iterator:
        if array[i] > array[i + 1]:
            (array[i], array[i + 1]) = (array[i + 1], array[i])
            swapped = True

    return swapped


# time: O(N^2); space: O(1)
# details: https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(array):
    size = len(array)
    swapped = True

    while swapped:
        swapped = _sorting_loop(array, size)
        size = size - 1


# time: O(N^2); space: O(1)
# details: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
def cocktail_shaker_sort(array):
    size = len(array)
    swapped = True

    while swapped:
        swapped = _sorting_loop(array, size)
        if swapped:
            swapped = _sorting_loop(array, size, forward=False)
            size = size - 1


# time: O(N^2); space: O(1)
# details: https://en.wikipedia.org/wiki/Selection_sort
def selection_sort(array):
    size = len(array)

    for i in range(size):
        ix_min = i
        for j in range(i + 1, size):
            if array[j] < array[ix_min]:
                ix_min = j

        if ix_min != i:
            (array[i], array[ix_min]) = (array[ix_min], array[i])


# time: O(N^2); space: O(1)
# details: https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(array):
    N = len(array)

    for i in range(1, N):
        pivot = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] <= pivot:
                break
            array[j + 1] = array[j]
        array[j] = pivot # j instead of j + 1 due to the break before


# TODO correct it!
def mergesort(array):
    helper = [None for _ in range(len(array))]
    _mergesort(array, helper, 0, len(array) - 1)

def _mergesort(array, helper, low, high):
    if low < high:
        middle = (low + high) // 2
        _mergesort(array, helper, low, middle)          # sort left half
        _mergesort(array, helper, middle + 1, high)     # sort right half
        merge(array, helper, low, middle, high)

def merge(array, helper, low, middle, high):
    for i in range(low, high + 1):
        helper[i] = array[i]

    left = cur = low
    right = middle + 1

    while (left <= middle) and (right <= high):
        if helper[left] <= helper[right]:
            array[cur] = helper[left]
            left += 1
        else:
            array[cur] = helper[right]
            right += 1
        cur += 1

    remaining = middle - left
    for i in range(0, remaining + 1):
        array[cur + i] = helper[left + 1]


# ### GRAPHS AND TREES


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


class TreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = TreeNode(value)

        elif value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = TreeNode(value)

    def depth(self):
        depth = 1
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0

        depth = 1 + max(left_depth, right_depth)
        return depth

    def __str__(self):
        return '{} => ({}, {})'.format(self.value, str(self.left), str(self.right))

def insert_into_tree(root, eltos):
    middle = len(eltos) // 2
    if not root:
        root = TreeNode(eltos[middle])
    else:
        root.add(eltos[middle])

    left = eltos[ : middle]
    if left:
        insert_into_tree(root, left)
    right = eltos[middle + 1 : ]
    if right:
        insert_into_tree(root, right)

    return root
