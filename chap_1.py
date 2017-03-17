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
    # time: O(N); space: O(1)
    def version_3(test):
        mask = 0

        for t in test:
            vector = 1 << (ord(t) - 97)
            if (mask & vector) == vector:
                return False
            mask = mask | vector

        return True

    tests = ["", "abcdefghijklmnopqrstuwvxyz", "abcdefghijklmnopqrstuwvxyza",
             "aabbcc", "mdifnafanfa", "aifasoid", "zyxvwutsrqponmlkjihgfedcba"]

    for test in tests:
        print("version 1 => '{}': {}".format(test, bool(version_1(test))))
        print("version 2 => '{}': {}".format(test, bool(version_2(test))))
        print("version 3 => '{}': {}".format(test, bool(version_3(test))))
        print()


def main(question):
    import sys

    print('##### Question {} #####'.format(question))

    module = sys.modules[__name__]
    getattr(module, 'question_{}'.format(question))()
