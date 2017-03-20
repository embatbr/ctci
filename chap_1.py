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


def main(question):
    import sys

    print('##### Question {} #####'.format(question))

    module = sys.modules[__name__]
    getattr(module, 'question_{}'.format(question))()
