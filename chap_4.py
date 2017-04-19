from utils import Node, Graph


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
