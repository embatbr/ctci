from utils import test_question, merge_sort


def question_0():
    print('##### Merge Sort #####\n')

    def version_1(test):
        (given, expected) = test

        sorted_given = given[:] # doesn't enter in the O(.) calculation
        merge_sort(sorted_given)

        return sorted_given == expected

    tests = [
        ([6, 3, 1, 7, 2, 8, 5, 4], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8])
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => {} sorted to {}" % version,
                          [test[0], test[1]],
                          locals()['version_%d' % version](test))
        print()


def question_1():
    print('##### Sorted Merge #####\n')

    def version_1(test):
        ((A, size_A, B), expected) = test

        ix_A = size_A - 1
        ix_B = len(B) - 1
        ix_merged = ix_A + ix_B + 1 # or size_A + len(B) - 1

        while ix_B >= 0:
            if (ix_A >= 0) and (A[ix_A] > B[ix_B]):
                A[ix_merged] = A[ix_A]
                ix_A -= 1
            else:
                A[ix_merged] = B[ix_B]
                ix_B -= 1
            ix_merged -= 1

        return A == expected

    tests = [
        (([1, 2, 3, None, None, None], 3, [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
        (([4, 5, 6, None, None, None], 3, [1, 2, 3]), [1, 2, 3, 4, 5, 6]),
        (([1, 4, 5, 19, None, None, None], 4, [2, 13, 30]), [1, 2, 4, 5, 13, 19, 30])
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => {} merged with {} equals to {}" % version,
                          [test[0][0][0 : test[0][1]], test[0][2], test[1]],
                          locals()['version_%d' % version](test))
        print()


def question_2():
    print('##### Group Anagrams #####\n')

    # time: # O(N*W*logW) (N = #word and W = avg size of a word)
    def version_1(test):
        (given, expected) = test

        anagrams = dict()
                                        # O(N*W*logW)
        for word in given:              # O(N)
            sorted_word = list(word)
            merge_sort(sorted_word)     # O(W*logW)
            sorted_word = ''.join(sorted_word)

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        keys = list(anagrams.keys())
        merge_sort(keys)

        sorted_words = list()

                                        # O(N*W*logW)
        for key in keys:                # O(1..N/p..N) (#keys <= N and p = #words/key)
            merge_sort(anagrams[key])   # O(W*logW)
            for word in anagrams[key]:  # O(N..p..1) (p = #words/key)
                sorted_words.append(word)

        return sorted_words == expected

    tests = [
        (['anagram', 'arara', 'aaagmnr', 'nagaram', 'arraa', 'ate', 'eta', 'eat'],
            ['aaagmnr', 'anagram', 'nagaram', 'arara', 'arraa', 'ate', 'eat', 'eta']),
        (['listen', 'admirer', 'silent', 'paternal', 'parental', 'married'],
            ['parental', 'paternal', 'admirer', 'married', 'listen', 'silent'])
    ]

    for test in tests:
        for version in range(1, 2):
            test_question("version %d => {} sorted to {}" % version,
                          [test[0], test[1]],
                          locals()['version_%d' % version](test))
        print()
