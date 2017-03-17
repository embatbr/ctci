"""Starting point.
"""


if __name__ == '__main__':
    import sys
    from importlib import import_module

    chapter = int(sys.argv[1])
    question = int(sys.argv[2])

    print('### CHAPTER {} ###\n'.format(chapter))

    module = import_module('chap_{}'.format(chapter))
    module.main(question)
