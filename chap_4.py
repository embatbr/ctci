from utils import Node, Graph, TreeNode


def question_1():
    print('##### Route Between Nodes #####\n')

    graph = Graph([Node(0), Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)],
                  [[1], [2], [0, 3], [2], [6], [4], [5]])

    def version_1(test):
        (source_value, target_value, dfs_expected, bfs_expected) = test
        source = graph.nodes[source_value]
        target = graph.nodes[target_value]

        graph.flush()
        dfs_path = graph.dfs(source, target)
        graph.flush()
        bfs_path = graph.bfs(source, target)

        return (dfs_path == dfs_expected) and (bfs_path == bfs_expected)

    tests = [
        (0, 0, [0], True),
        (0, 1, [0, 1], True),
        (0, 3, [0, 1, 2, 3], True),
        (4, 5, [4, 6, 5], True),
        (1, 4, list(), False)
    ]

    for test in tests:
        print('version 1 => path from {} to {} is {}: {}'.format(test[0], test[1], test[2],
                                                                 version_1(test)))
        print()


def question_2():
    print('##### Minimal Tree #####\n')

    def version_1(test):
        (given, expected) = test

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

        root = None
        if given:
            root = insert_into_tree(root, given)

        depth = root.depth() if root else 0

        return depth == expected

    tests = [
        (list(), 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        (list(range(1, 11)), 4),
        (list(range(1, 16)), 4),
        (list(range(1, 20)), 5)
    ]

    for test in tests:
        print('version 1 => list {} makes a tree with minimal depth {}: {}'.format(test[0], test[1],
                                                                                   version_1(test)))
        print()
