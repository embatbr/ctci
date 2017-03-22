"""Starting point.
"""


if __name__ == '__main__':
    import sys
    from importlib import import_module

    chapter = int(sys.argv[1])
    question = int(sys.argv[2])

    print('### CHAPTER {} ###\n\n##### Question {} #####'.format(chapter, question))

    module = import_module('chap_{}'.format(chapter))
    getattr(module, 'question_{}'.format(question))()
