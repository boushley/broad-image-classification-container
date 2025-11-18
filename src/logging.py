import os

def verbose(*args, **kwargs):
    if 'VERBOSE' in os.environ and (os.environ['VERBOSE'] == '1' or os.environ['VERBOSE'] == 'true'):
        print(*args, **kwargs)
