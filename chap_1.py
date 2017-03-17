def question_1():
    print('##### Is Unique #####\n')

    # time: O(N**2); space: O(1)
    def version_1(test):
        size = len(test)

        for i in range(size):
            for j in range(i + 1, size):
                if test[i] == test[j]:
                    return False

        return True

    # time: O(N); space: O(N)
    def version_2(test):
        chars = set()

        for t in test:
            if t in chars:
                return False
            chars.add(t)

        return True

    # considers only lowercase letters
    # hint #117
    # time: O(N); space: O(1)
    def version_3(test):
        mask = 0

        for t in test:
            vector = 1 << (ord(t) - 97)
            if (mask & vector) == vector:
                return False
            mask = mask | vector

        return True

    tests = ['', 'abcdefghijklmnopqrstuwvxyz', 'abcdefghijklmnopqrstuwvxyza',
             'aabbcc', 'mdifnafanfa', 'aifasoid', 'zyxvwutsrqponmlkjihgfedcba']

    for test in tests:
        print("version 1 => '{}': {}".format(test, bool(version_1(test))))
        print("version 2 => '{}': {}".format(test, bool(version_2(test))))
        print("version 3 => '{}': {}".format(test, bool(version_3(test))))
        print()


def question_2():
    print('##### Check Permutation #####\n')

    # time: O(A*logA + B*logB); space: O(A + B)
    def version_1(test):
        A = test[0]
        B = test[1]

        if len(A) != len(B):
            return False

        return sorted(A) == sorted(B)

    # time: O(A), if A and B have the same length; space: O(a + b), with a and b the sizes of stats_A and stats_B
    def version_2(test):
        A = test[0]
        B = test[1]

        if len(A) != len(B):
            return False

        stats_A = dict()
        stats_B = dict()

        for i in range(len(A)):
            A_i = A[i]
            if A_i not in stats_A:
                stats_A[A_i] = 0
            stats_A[A_i] += 1

            B_i = B[i]
            if B_i not in stats_B:
                stats_B[B_i] = 0
            stats_B[B_i] += 1

        return stats_A == stats_B

    tests = [('', ''), ('aabbcc', 'abc'), ('abcaa', 'abcaa'), ('abc', 'bca'),
             ('abc', 'bda'), ('aabccc', 'aabccccccc')]

    for test in tests:
        print("version 1 => '{}' is permutation of '{}': {}".format(test[0],
            test[1], version_1(test)))
        print("version 2 => '{}' is permutation of '{}': {}".format(test[0],
            test[1], version_2(test)))
        print()


def question_3():
    print('##### URLify #####\n');

    # time: O(length); space: O(N)
    def version_1(test):
        chars = list(test[0]) # doesn't count in the O(.) calculation
        length = test[1]

        output = [''] * len(chars)

        j = 0
        for i in range(length):
            c = chars[i]
            if c == ' ':
                output[j] = '%'
                output[j + 1] = '2'
                output[j + 2] = '0'
                j += 3
            else:
                output[j] = c
                j += 1

        return ''.join(output) # doesn't count in the O(.) calculation

    # time: O(length); space: O(1)
    def version_2(test):
        chars = list(test[0]) # doesn't count in the O(.) calculation
        length = test[1]

        i = length - 1
        j = len(chars) - 1
        while i >= 0:
            c = chars[i]
            if c == ' ':
                chars[j] = '0'
                chars[j - 1] = '2'
                chars[j - 2] = '%'
                j -= 3
            else:
                chars[j] = c
                j -= 1

            i -= 1

        chars = chars[j + 1 : ]
        return ''.join(chars) # doesn't count in the O(.) calculation

    tests = [('Mr John Smith        ', 13), (' Mr   John Smith                 ', 18),
             ('        ', 2), ('    ', 0), ('Mr   John Smith            ', 15)]

    for test in tests:
        print("version 1 => '{}' URLfied first {} chars to '{}'".format(test[0],
            test[1], version_1(test)))
        print("version 2 => '{}' URLfied first {} chars to '{}'".format(test[0],
            test[1], version_2(test)))
        print()


def main(question):
    import sys

    print('##### Question {} #####'.format(question))

    module = sys.modules[__name__]
    getattr(module, 'question_{}'.format(question))()
