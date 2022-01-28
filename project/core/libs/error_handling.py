
from datetime import datetime
from inspect import currentframe, getframeinfo

filename = 'log'


def write_in_log(a, e):
    with open(filename, 'a+') as f:
        f.write(f"\n{datetime.now()}: {e} \n {a}\n\n")
