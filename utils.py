"""Code useful in many places.
"""


import math


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


# time: O(N); space: O(1)
# auxiliar function for bubble and cocktail shaker sorts
# param forward == False only happens for cocktail shaker sort
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


# time: O(N); space: O(1)
def _copy_array(source, ix_source, target, ix_target, num_iterations):
    for _ in range(num_iterations):
        target[ix_target] = source[ix_source]
        ix_target += 1
        ix_source += 1

# time: O(N); space: O(1) (the 'aux' array is part of the input)
def _combine(array, aux, ix_begin, ix_middle, ix_end):
    ix_left = ix_begin
    ix_right = ix_middle + 1
    ix_aux = ix_begin

    while (ix_left <= ix_middle) and (ix_right <= ix_end):
        left = array[ix_left]
        right = array[ix_right]

        if right < left:
            aux[ix_aux] = right
            ix_right += 1
        else:
            aux[ix_aux] = left
            ix_left += 1
        ix_aux += 1

    # the first two lines are mutually exclusive
    _copy_array(array, ix_left, aux, ix_aux, ix_middle - ix_left + 1)
    _copy_array(array, ix_right, aux, ix_aux, ix_end - ix_right + 1)
    _copy_array(aux, ix_begin, array, ix_begin, ix_end - ix_begin + 1)

# time: O(logN); space: O(1) (the 'aux' array is part of the input)
def _divide(array, aux, ix_begin, ix_end):
    if ix_begin < ix_end:
        ix_middle = (ix_begin + ix_end) // 2
        _divide(array, aux, ix_begin, ix_middle)
        _divide(array, aux, ix_middle + 1, ix_end)

        _combine(array, aux, ix_begin, ix_middle, ix_end)

# time: O(N*logN); space: O(N) (the 'aux' array is created here)
def merge_sort(array):
    _divide(array, list(array), 0, len(array) - 1)


# time: O(N); space: O(1)
def _partition(array, ix_low, ix_hi, pivot):
    while ix_low <= ix_hi:
        while array[ix_low] < pivot:
            ix_low += 1
        while array[ix_hi] > pivot:
            ix_hi -= 1

        if ix_low <= ix_hi:
            (array[ix_low], array[ix_hi]) = (array[ix_hi], array[ix_low])
            ix_low += 1
            ix_hi -= 1

    return ix_low

# time: O(N*logN); space: O(1)
def _quick_sort(array, ix_low, ix_hi):
    if ix_low < ix_hi:
        ix_pivot = (ix_low + ix_hi) // 2
        pivot = array[ix_pivot]
        index = _partition(array, ix_low, ix_hi, pivot)
        _quick_sort(array, ix_low, index - 1)
        _quick_sort(array, index, ix_hi)

# time: O(N*logN); space: O(1)
def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)


# time: O(K*N) (where K is the number of k values); space: O(N)
def radix_sort(array):
    size = len(array)
    k = 1
    highest = max(array)

    while k < highest:
        buckets = dict()

        for elto in array:
            key = 0 if elto < k else (elto % (k * 10)) // k

            if key in buckets:
                buckets[key].append(elto)
            else:
                buckets[key] = [elto]

        better_sorted_array = list()

        for key in range(10):
            if key in buckets:
                bucket = buckets[key]
                better_sorted_array.extend(bucket)

        array = better_sorted_array
        k = k * 10

    return array


# ### HEAP ###


class HeapOverflowError(Exception):

    def __init__(self):
        self.message = 'Heap has reached maximum capacity.'


class HeapUnderflowError(Exception):

    def __init__(self):
        self.message = 'Heap is empty.'


class Heap(object):

    def __init__(self, depth=None):
        self._capacity = 0
        self._size = 0
        self._array = None

        if depth and isinstance(depth, int):
            self._flush(depth)

    def _flush(self, depth):
        self._capacity = 2**depth - 1
        self._size = 0
        self._array = [None] * self._capacity

    def add(self, value):
        if self._size == self._capacity:
            raise HeapOverflowError()

        self._array[self._size] = value
        index = self._size
        self._size = self._size + 1

        return index

    def remove(self, index):
        if (0 > index) or (index >= self._size):
            raise HeapUnderflowError()

        value = self._array[index]
        if index < (self._size - 1):
            self._array[index] = self._array[self._size - 1]
        self._array[self._size - 1] = None

        self._size = self._size - 1

        return value

    # time: O(N), when is a simple heap, or O(N*logN), when is a sorted heap; space: O(1)
    def heapify(self, array):
        capacity = len(array)
        depth = math.ceil(math.log2(capacity + 1))
        self._flush(depth)

        for x in array:
            self.add(x)

    def parent_index(self, index):
        if index > 0:
            return (index - 1) // 2
        return None

    def left_child_index(self, index):
        child_index = 2 * index + 1
        if child_index < self._size:
            return child_index
        return None

    def right_child_index(self, index):
        child_index = 2 * index + 2
        if child_index < self._size:
            return child_index
        return None

    def _to_str(self, index):
        if index >= self._size:
            return ''

        left = self._to_str(index*2 + 1)
        left = left if left == '' else ' ({})'.format(left)
        right = self._to_str(index*2 + 2)
        right = right if right == '' else ' ({})'.format(right)
        return '{}{}{}'.format(self._array[index], left, right)


    def __str__(self):
        return self._to_str(0)


class SortedHeap(Heap):

    def __init__(self, depth=None, func=None):
        super(SortedHeap, self).__init__(depth)

        self._func = func

    # time: O(logN); space: O(1)
    def _heapify_down(self, index):
        child_ix = self.left_child_index(index)

        while child_ix:
            right_child_ix = self.right_child_index(index)
            if right_child_ix and self._func(self._array[right_child_ix], self._array[child_ix]):
                child_ix = right_child_ix

            if self._func(self._array[index], self._array[child_ix]):
                break

            (self._array[index], self._array[child_ix]) = (self._array[child_ix], self._array[index])

            index = child_ix
            child_ix = self.left_child_index(index)

    # time: O(logN); space: O(1)
    def _heapify_up(self):
        index = self._size - 1
        parent_index = self.parent_index(index)

        while (index > 0) and (self._func(self._array[index], self._array[parent_index])):
            value = self._array[index]
            self._array[index] = self._array[parent_index]
            self._array[parent_index] = value

            index = parent_index
            parent_index = self.parent_index(index)

    def add(self, value):
        index = super(SortedHeap, self).add(value)

        self._heapify_up()

        return index

    def remove(self, index):
        value = super(SortedHeap, self).remove(index)

        self._heapify_down(index)

        return value


class MinHeap(SortedHeap):

    def __init__(self, depth=None):
        super(MinHeap, self).__init__(depth, lambda x, y: x < y)


class MaxHeap(SortedHeap):

    def __init__(self, depth=None):
        super(MaxHeap, self).__init__(depth, lambda x, y: x > y)


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
