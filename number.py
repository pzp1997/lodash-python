import random

def clamp(number, lower, upper, min=min, max=max):
    return min(max(lower, number), upper)

def inRange(number, start=0, end=0):
    if start > end:
        start, end = end, start
    return number >= start and number < end

def random(lower=None, upper=None, floating=False, type=type, rand=random.randrange):
    if lower is None and upper is None:
        lower, upper = 0, 1
    elif upper is None:
        upper, lower = lower, 0
    elif lower is None:
        lower = 0

    if type(lower) == float or type(upper) == float:
        floating = True

    randrange(lower, upper)
