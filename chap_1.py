from copy import deepcopy

from utils import test_question, show_matrix, check_test


def question_1():
    print('##### Is Unique #####\n')

    # time: O(N**2); space: O(1)
    # no additional structures used
    def version_1(test):
        (given, expected) = test

        size = len(given)

        for i in range(size):
            for j in range(i + 1, size):
                if given[i] == given[j]:
                    return expected == False

        return expected == True

    # time: O(N); space: O(N)
    # using a hash set
    def version_2(test):
        (given, expected) = test

        chars = set()

        for t in given:
            if t in chars:
                return expected == False
            chars.add(t)

        return expected == True

    # time: O(N); space: O(1)
    # using a bit mask (hint 117; considers only lowercase letters)
    def version_3(test):
        (given, expected) = test

        mask = 0

        for t in given:
            vector = 1 << (ord(t) - 97)
            if (mask & vector) == vector:
                return expected == False
            mask = mask | vector

        return expected == True

    tests = [
        ('', True),
        ('abcdefghijklmnopqrstuwvxyz', True),
        ('abcdefghijklmnopqrstuwvxyza', False),
        ('aabbcc', False),
        ('mdifnafanfa', False),
        ('aifasoid', False),
        ('zyxvwutsrqponmlkjihgfedcba', True)
    ]

    for test in tests:
        for version in range(1, 4):
            test_question("version %d => '{}' is {}unique" % version,
                          [test[0], '' if test[1] else 'NOT '],
                          locals()['version_%d' % version](test))
        print()


def question_2():
    print('##### Check Permutation #####\n')

    # time: O(A*logA + B*logB); space: O(A + B)
    # Python uses Timsort, with worst cases: O(N*logN) and O(N) for time and space, respectively
    def version_1(test):
        (A, B, expected) = test

        if len(A) != len(B):
            return expected == False

        return expected == (sorted(A) == sorted(B))

    # time: O(len(A)); space: O(len(A))
    # worst case complexity only happens when A and B have the same length
    def version_2(test):
        (A, B, expected) = test

        if len(A) != len(B):
            return expected == False

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

        return expected == (stats_A == stats_B)

    tests = [
        ('', '', True),
        ('aabbcc', 'abc', False),
        ('abcaa', 'abcaa', True),
        ('abc', 'bca', True),
        ('abc', 'bda', False),
        ('aabccc', 'aabccccccc', False)]

    for test in tests:
        for version in range(1, 3):
            test_question("version %d => '{}' is {}permutation of '{}'" % version,
                          [test[0], '' if test[2] else 'NOT ', test[1]],
                          locals()['version_%d' % version](test))
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
    # replaces ' ' by '%20' in place (assuming it has enough space after the word)
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

    tests = [
        ('Mr John Smith        ', 13, 'Mr%20John%20Smith'),
        (' Mr   John Smith                 ', 18, '%20Mr%20%20%20John%20Smith%20%20'),
        ('        ', 2, '%20%20'),
        ('    ', 0, ''),
        ('Mr   John Smith            ', 15, 'Mr%20%20%20John%20Smith')
    ]

    for test in tests:
        for version in range(1, 3):
            test_question("version %d => '{}' URLfied first {} chars to '{}'" % version,
                          [test[0], test[1], test[2]],
                          locals()['version_%d' % version](test))
        print()


def question_4():
    print('##### Palindrome Permutation #####\n')

    # time: O(N); space: O(N)
    # using hash sets
    def version_1(test):
        (given, expected) = test

        odds = set()
        evens = set()

        given = given.lower() # O(N)
        for t in given:
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

        return (len(odds) <= 1) == expected

    # time: O(N); space: O(1)
    # using bit masks
    def version_2(test):
        (given, expected) = test

        odds = 0
        evens = 0

        given = given.lower() # O(N)
        for t in given:
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
                return False == expected

        return (num_odds_bits <= 1) == expected

    tests = [
        ('Tact Coa', True),
        ('arara', True),
        ('casa', False),
        ('', True),
        ('palindrome', False),
        ('Madam I\'m Adam', True),
        ('Madam I am Adam', False),
        ('coco', True)
    ]

    for test in tests:
        for version in range(1, 3):
            test_question("version %d => '{}' does {}have palindrome permutation" % version,
                          [test[0], '' if test[1] else 'NOT '],
                          locals()['version_%d' % version](test))
        print()


def question_5():
    print('##### One Away #####\n')

    # time: O(N), where N is the size of the smaller string; space: O(1)
    def version_1(test):
        original = test[0]
        edited = test[1]
        expected = test[2]

        diff_len = len(original) - len(edited)

        if diff_len == 0: # possible replace
            num_diffs = 0

            # time: O(N)
            for i in range(len(original)):
                if original[i] != edited[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    return False == expected

            return True == expected

        elif diff_len == 1: # possible removal
            i = j = 0

            # time: O(N), where N is the length of edited
            while (i < len(original)) and (j < len(edited)):
                if original[i] == edited[j]:
                    j += 1
                i += 1

                if i - j == 2:
                    return False == expected

            return True == expected

        elif diff_len == -1: # possible insertion
            i = j = 0

            # time: O(N), where N is the length of original
            while (i < len(original)) and (j < len(edited)):
                if original[i] == edited[j]:
                    i += 1
                j += 1

                if i - j == -2:
                    return False == expected

            return True == expected

        return False == expected

    # time: O(N), where N is the size of the smaller string; space: O(1)
    def version_2(test):
        original = test[0]
        edited = test[1]
        expected = test[2]

        diff_len = len(original) - len(edited)

        if diff_len == 0: # possible replace
            num_diffs = 0

            # time: O(N)
            for i in range(len(original)):
                if original[i] != edited[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    return False == expected

            return True == expected

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
                    return False == expected

            return True == expected

        return False == expected

    # time: O(N), where N is the size of the smaller string; space: O(1)
    def version_3(test):
        original = test[0]
        edited = test[1]
        expected = test[2]

        diff_len = len(original) - len(edited)

        if diff_len < -1 or diff_len > 1:
            return False == expected

        num_diffs = i = j = 0
        while (i < len(original)) and (j < len(edited)):
            if diff_len == 0:
                if original[i] != edited[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    return False == expected

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
                    return False == expected

        return True == expected

    tests = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pales', 'bale', False),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('ball', 'balls', True),
        ('ball', 'ballss', False),
        ('ball', 'calls', False),
        ('ball', 'cball', True),
        ('ball', 'cballss', False),
        ('ball', 'call', True)
    ]

    for test in tests:
        for version in range(1, 4):
            test_question("version %d => '{}' is {}one way to '{}'" % version,
                          [test[0], '' if test[2] else 'NOT ', test[1]],
                          locals()['version_%d' % version](test))
        print()


def question_6():
    print('##### String Compression #####\n')

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

    tests = [
        ('abc', 'abc'),
        ('aabbcc', 'aabbcc'),
        ('aabbccc', 'a2b2c3'),
        ('aabcccccaaa', 'a2b1c5a3')
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => '{}' is compressed to '{}'" % version,
                          [test[0], test[1]],
                          locals()['version_%d' % version](test))
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
        for version in range(1, 2):
            test_question("version %d =>\nmatrix\n\n {}\nrotated to\n\n {}\n" % version,
                          [show_matrix(test[0]), show_matrix(test[1])],
                          locals()['version_%d' % version](test))
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
        for version in range(1, 4):
            test_copy = deepcopy(test)
            print("version %d =>\nmatrix\n" % version)
            print('', show_matrix(test_copy[0]))
            result = version_1(test_copy)
            print('rotated to\n')
            print('', show_matrix(test_copy[1]))
            print(check_test(result))
            print()


def question_9():
    print('##### String Rotation #####\n')

    # time: O(N); space: O(N) (considering the indexed strings must be copied)
    def version_1(test):
        given = test[0]
        rotated = test[1]
        expected = test[2]

        if len(given) != len(rotated):
            return False == expected

        for i in range(len(given)):
            i_comp = len(rotated) - i

            if given[i : ] == rotated[ : i_comp] and rotated[i_comp : ] == given[ : i]:
                return True == expected

        return False == expected

    def version_2(test):
        given = test[0]
        rotated = test[1]
        expected = test[2]

        if len(given) != len(rotated):
            return False == expected

        i = j = 0
        found_first_equal = False
        while j < len(rotated):
            g = given[i]
            e = rotated[j]

            i = (i + 1) % len(given)

            if g == e:
                found_first_equal = True
                j += 1

                if j > len(given):
                    return False == expected

            if found_first_equal and (g != e):
                return False == expected

        return True == expected

    tests = [
        ('waterbottle', 'erbottlewat', True),
        ('waterbottle', 'erbottlehov', False),
        ('waterbottle', 'bottlewater', True),
        ('waterbottle', 'bottlehover', False),
        ('waterbottle', 'bottlewaters', False),
        ('waterbottle', 'erbottlewaterbottlewat', False),
        ('erbottlewaterbottlewat', 'waterbottle', False),
        ('erbottlewaterbottlewat', 'erbottlewat', False)
    ]

    for test in tests:
        for version in range(1, 3):
            test_question("version %d => '{}' is {}a rotation of '{}'" % version,
                          [test[0], '' if test[2] else 'NOT ', test[1]],
                          locals()['version_%d' % version](test))
        print()
