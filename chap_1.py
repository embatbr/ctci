from copy import deepcopy
from utils import show_matrix


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
        print("version 1 => '{}' is unique: {}".format(test, version_1(test)))
        print("version 2 => '{}' is unique: {}".format(test, version_2(test)))
        print("version 3 => '{}' is unique: {}".format(test, version_3(test)))
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
        expected = test[2]

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

        chars = ''.join(output) # doesn't count in the O(.) calculation

        return chars == expected

    # time: O(length); space: O(1)
    def version_2(test):
        chars = list(test[0]) # doesn't count in the O(.) calculation
        length = test[1]
        expected = test[2]

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
        chars = ''.join(chars) # doesn't count in the O(.) calculation

        return chars == expected

    tests = [('Mr John Smith        ', 13, 'Mr%20John%20Smith'),
             (' Mr   John Smith                 ', 18, '%20Mr%20%20%20John%20Smith%20%20'),
             ('        ', 2, '%20%20'), ('    ', 0, ''),
             ('Mr   John Smith            ', 15, 'Mr%20%20%20John%20Smith')]

    for test in tests:
        print("version 1 => '{}' URLfied first {} chars to '{}': {}".format(test[0],
            test[1], test[2], version_1(test)))
        print("version 2 => '{}' URLfied first {} chars to '{}': {}".format(test[0],
            test[1], test[2], version_2(test)))
        print()


def question_4():
    print('##### Palindrome Permutation #####\n')

    # time: O(N); space: O(N)
    def version_1(test):
        odds = set()
        evens = set()

        test = test.lower() # O(N)
        for t in test:
            c = ord(t)
            if ord('a') <= c <= ord('z'):
                if c in odds:
                    odds.remove(c)
                    evens.add(c)
                elif c in evens:
                    evens.remove(c)
                    odds.add(c)
                else: # 1st time
                    odds.add(c)

        return len(odds) <= 1

    # time: O(N); space: O(1)
    def version_2(test):
        odds = 0
        evens = 0

        test = test.lower() # O(N)
        for t in test:
            c = ord(t)
            if ord('a') <= c <= ord('z'):
                vec = 1 << (c - 97)
                if (odds & vec) == vec:
                    odds = odds ^ vec
                    evens = evens | vec
                elif (evens & vec) == vec:
                    evens = evens ^ vec
                    odds = odds | vec
                else:
                    odds = odds | vec

        num_odds_bits = 0
        for i in range(ord('z') - ord('a') + 1):
            vec = 1 << i
            if (odds & vec) == vec:
                num_odds_bits += 1
            if num_odds_bits > 1:
                return False

        return num_odds_bits <= 1

    tests = ['Tact Coa', 'arara', 'casa', '', 'palindrome', 'Madam I\'m Adam',
             'Madam I am Adam', 'coco']

    for test in tests:
        print("version 1 => '{}' has palindrome permutation: {}".format(test,
            version_1(test)))
        print("version 2 => '{}' has palindrome permutation: {}".format(test,
            version_2(test)))
        print()


def question_5():
    print('##### One Away #####\n')

    # time: O(N), where N is the size of the smaller string; space: O(1)
    def version_1(test):
        original = test[0]
        edited = test[1]
        diff_len = len(original) - len(edited)

        if diff_len == 0: # possible replace
            num_diffs = 0

            # time: O(N)
            for i in range(len(original)):
                if original[i] != edited[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    return False

            return True

        elif diff_len == 1: # possible removal
            i = j = 0

            # time: O(N), where N is the length of edited
            while (i < len(original)) and (j < len(edited)):
                if original[i] == edited[j]:
                    j += 1
                i += 1

                if i - j == 2:
                    return False

            return True

        elif diff_len == -1: # possible insertion
            i = j = 0

            # time: O(N), where N is the length of original
            while (i < len(original)) and (j < len(edited)):
                if original[i] == edited[j]:
                    i += 1
                j += 1

                if i - j == -2:
                    return False

            return True

        return False

    # time: O(N), where N is the size of the smaller string; space: O(1)
    def version_2(test):
        original = test[0]
        edited = test[1]
        diff_len = len(original) - len(edited)

        if diff_len == 0: # possible replace
            num_diffs = 0

            # time: O(N)
            for i in range(len(original)):
                if original[i] != edited[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    return False

            return True

        elif (diff_len == 1) or (diff_len == -1): # possible removal or insertion
            i = j = 0

            while (i < len(original)) and (j < len(edited)):
                if original[i] == edited[j]:
                    i += 1
                    j += 1
                else:
                    if diff_len == 1:
                        i += 1
                    else:
                        j += 1

                if (diff_len == 1 and i - j == 2) or (diff_len == -1 and i - j == -2):
                    return False

            return True

        return False

    # time: O(N), where N is the size of the smaller string; space: O(1)
    def version_3(test):
        original = test[0]
        edited = test[1]
        diff_len = len(original) - len(edited)

        if diff_len < -1 or diff_len > 1:
            return False

        num_diffs = i = j = 0
        while (i < len(original)) and (j < len(edited)):
            if diff_len == 0:
                if original[i] != edited[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    return False

                i += 1
                j += 1
            else:
                if original[i] == edited[j]:
                    i += 1
                    j += 1
                else:
                    if diff_len == 1:
                        i += 1
                    else:
                        j += 1

                if (diff_len == 1 and i - j == 2) or (diff_len == -1 and i - j == -2):
                    return False

        return True

    tests = [('pale', 'ple'), ('pales', 'pale'), ('pales', 'bale'), ('pale', 'bale'),
             ('pale', 'bake'), ('ball', 'balls'), ('ball', 'ballss'), ('ball', 'calls'),
             ('ball', 'cball'), ('ball', 'cballss'), ('ball', 'call')]

    for test in tests:
        print("version 1 => '{}' is on way to '{}': {}".format(test[0], test[1],
            version_1(test)))
        print("version 2 => '{}' is on way to '{}': {}".format(test[0], test[1],
            version_2(test)))
        print("version 3 => '{}' is on way to '{}': {}".format(test[0], test[1],
            version_3(test)))
        print()


def question_6():
    print('##### String Compression #####\n')

    tests = [('abc', 'abc'), ('aabbcc', 'aabbcc'), ('aabbccc', 'a2b2c3'),
             ('aabcccccaaa', 'a2b1c5a3')]

    # time: O(N) or O(N*d), where O(d) is the order to turn int into string; space: O(N)
    def version_1(test):
        given = test[0]
        expected = test[1]

        compressed = ''
        cur = prev = given[0]
        i = freq = 0

        while i <= len(given):
            cur = given[i] if i < len(given) else None
            if i < len(given) and cur == prev:
                freq += 1
            else:
                compressed = '{}{}{}'.format(compressed, prev, freq)
                freq = 1

            prev = cur
            i += 1

        final = compressed if len(compressed) < len(given) else given

        return final == expected

    for test in tests:
        print("version 1 => '{}' is compressed to '{}': {}".format(test[0], test[1],
            version_1(test)))
        print()


def question_7():
    print('##### Rotate Matrix #####\n')

    def version_1(test):
        given = test[0]
        expected = test[1]

        size = len(given)
        middled = int(size / 2)

        end = size - 1
        for i in range(middled):
            for j in range(i, end - i):
                upper_left_line = i
                upper_left_column = j % size
                upper_left_value = given[upper_left_line][upper_left_column]

                bottom_left_line = end - j
                bottom_left_column = i % size
                given[upper_left_line][upper_left_column] = given[bottom_left_line][bottom_left_column]

                bottom_right_line = end - i
                bottom_right_column = end - j
                given[bottom_left_line][bottom_left_column] = given[bottom_right_line][bottom_right_column]

                upper_right_line = j
                upper_right_column = end - i
                given[bottom_right_line][bottom_right_column] = given[upper_right_line][upper_right_column]

                given[upper_right_line][upper_right_column] = upper_left_value;

        return given == expected

    tests = [
        ([['1-1']], [['1-1']]),
        ([['1-1', '1-2', '1-3', '1-4'], ['2-1', '2-2', '2-3', '2-4'], ['3-1', '3-2', '3-3', '3-4'],
            ['4-1', '4-2', '4-3', '4-4']],
         [['4-1', '3-1', '2-1', '1-1'], ['4-2', '3-2', '2-2', '1-2'], ['4-3', '3-3', '2-3', '1-3'],
            ['4-4', '3-4', '2-4', '1-4']]),
        ([['1-1', '1-2', '1-3', '1-4', '1-5'], ['2-1', '2-2', '2-3', '2-4', '2-5'], ['3-1', '3-2', '3-3', '3-4', '3-5'],
            ['4-1', '4-2', '4-3', '4-4', '4-5'], ['5-1', '5-2', '5-3', '5-4', '5-5']],
         [['5-1', '4-1', '3-1', '2-1', '1-1'], ['5-2', '4-2', '3-2', '2-2', '1-2'], ['5-3', '4-3', '3-3', '2-3', '1-3'],
            ['5-4', '4-4', '3-4', '2-4', '1-4'], ['5-5', '4-5', '3-5', '2-5', '1-5']])
    ]

    for test in tests:
        print("version 1 =>\nmatrix")
        show_matrix(test[0])
        result = version_1(test)
        print("rotated to")
        show_matrix(test[1])
        print(result)
        print()


def question_8():
    print('##### Zero Matrix #####\n')

    # time: O(M*N); space: O(M*N + M + N)
    def version_1(test):
        given = test[0]
        expected = test[1]

        num_lines = len(given)
        num_columns = len(given[0])

        output = deepcopy(given)
        zeroed_lines = set()
        zeroed_columns = set()

        for i in range(num_lines):
            for j in range(num_columns):
                elto = given[i][j]
                if elto == 0:
                    zeroed_lines.add(i)
                    zeroed_columns.add(j)

        for i in range(num_lines):
            for j in range(num_columns):
                if i in zeroed_lines or j in zeroed_columns:
                    output[i][j] = 0

        return output == expected

    # time: O(M*N); space: O(M + N)
    def version_2(test):
        given = test[0]
        expected = test[1]

        num_lines = len(given)
        num_columns = len(given[0])

        zeroed_lines = set()
        zeroed_columns = set()

        for i in range(num_lines):
            for j in range(num_columns):
                elto = given[i][j]
                if elto == 0:
                    zeroed_lines.add(i)
                    zeroed_columns.add(j)

        for i in range(num_lines):
            for j in range(num_columns):
                if i in zeroed_lines or j in zeroed_columns:
                    given[i][j] = 0

        return given == expected

    # time: O(M*N); space: O(1)
    def version_3(test):
        given = test[0]
        expected = test[1]

        num_lines = len(given)
        num_columns = len(given[0])

        zeroed_lines = 0
        zeroed_columns = 0

        for i in range(num_lines):
            for j in range(num_columns):
                elto = given[i][j]
                if elto == 0:
                    zeroed_lines |= 1 << i
                    zeroed_columns |= 1 << j

        for i in range(num_lines):
            for j in range(num_columns):
                vec_lines = 1 << i
                vec_columns = 1 << j

                if (zeroed_lines & vec_lines == vec_lines) or (zeroed_columns & vec_columns == vec_columns):
                    given[i][j] = 0

        return given == expected

    tests = [
        ([[0, 2, 0], [4, 5, 0], [7, 8, 9]], [[0, 0, 0], [0, 0, 0], [0, 8, 0]]),
        ([[1, 0], [3, 4], [5, 0], [7, 8]], [[0, 0], [3, 0], [0, 0], [7, 0]]),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 0, 15]],
            [[1, 2, 3, 0, 5], [6, 7, 8, 0, 10], [0, 0, 0, 0, 0]])
    ]

    for test in tests:
        print("version 1 =>\nmatrix")
        show_matrix(test[0])
        result = version_1(test)
        print('rotated to')
        show_matrix(test[1])
        print(result)
        print()

        test_version_2 = deepcopy(test)
        print("version 2 =>\nmatrix")
        show_matrix(test_version_2[0])
        result = version_2(test_version_2)
        print('rotated to')
        show_matrix(test_version_2[1])
        print(result)
        print()

        test_version_3 = deepcopy(test)
        print("version 3 =>\nmatrix")
        show_matrix(test_version_3[0])
        result = version_3(test_version_3)
        print('rotated to')
        show_matrix(test_version_3[1])
        print(result)
        print()


def question_9():
    print('##### String Rotation #####\n')

    # time: O(N); space: O(N) (considering the indexed strings must be copied)
    def version_1(test):
        given = test[0]
        expected = test[1]

        if len(given) != len(expected):
            return False

        for i in range(len(given)):
            i_comp = len(expected) - i

            if given[i : ] == expected[ : i_comp] and expected[i_comp : ] == given[ : i]:
                return True

        return False

    def version_2(test):
        given = test[0]
        expected = test[1]

        if len(given) != len(expected):
            return False

        i = j = 0
        found_first_equal = False
        while j < len(expected):
            g = given[i]
            e = expected[j]

            i = (i + 1) % len(given)

            if g == e:
                found_first_equal = True
                j += 1

                if j > len(given):
                    return False

            if found_first_equal and (g != e):
                return False

        return True

    tests = [('waterbottle', 'erbottlewat'), ('waterbottle', 'erbottlehov'),
             ('waterbottle', 'bottlewater'), ('waterbottle', 'bottlehover'),
             ('waterbottle', 'bottlewaters'), ('waterbottle', 'erbottlewaterbottlewat'),
             ('erbottlewaterbottlewat', 'waterbottle'), ('erbottlewaterbottlewat', 'erbottlewat')]

    for test in tests:
        print("version 1 => '{}' is a rotation of '{}': {}".format(test[0], test[1], version_1(test)))
        print("version 2 => '{}' is a rotation of '{}': {}".format(test[0], test[1], version_2(test)))
        print()


def main(question):
    import sys

    print('##### Question {} #####'.format(question))

    module = sys.modules[__name__]
    getattr(module, 'question_{}'.format(question))()
