import sys


def convert(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}" \
            .format(str(e)),
            file=sys.stderr)
    return -1

# IndentationError, SyntaxError and NameError: You should NOT normally catch this!

import os

def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally: #finally-block is executed no matter how the try-block exits
        os.chdir(original_path)
