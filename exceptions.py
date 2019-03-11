def convert(s):
    '''Convert to an integer'''
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except (ValueError, TypeError):
        print("Conversion failed!")
        x = -1
    return x

# IndentationError, SyntaxError and NameError: You should NOT normally catch this!
