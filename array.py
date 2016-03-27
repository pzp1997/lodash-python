import itertools

def chunk(arr, size=1, fillvalue=None, izip=itertools.izip_longest, iter=iter):
    return izip(*[iter(arr)]*size, fillvalue=None)

def compact(arr, ifilter=itertools.ifilter, bool=bool):
    return ifilter(bool, arr)

def concat(arr, *values):
    copy = arr[:]
    copy.extend(values)
    return copy

def difference():
    pass

def differenceBy():
    pass

def differenceWith():
    pass

def drop(arr, n=1):
    return arr[n:]

def dropRight(arr, n=1):
    return arr[:-n] if n > 0 else arr[:]

def dropRightWhile():
    pass

def dropWhile():
    pass

def fill(arr, val, start=0, end=None):
    if end is None: end = len(arr)
    return arr[:start] + [val] * (end-start) + arr[end:]

def findIndex():
    pass

def findLastIndex():
    pass

first = head

def flatten():
    pass

def flattenDeep():
    pass

def flattenDepth():
    pass

fromPairs = dict

def head(arr):
    return arr[0]

def indexOf(arr, value, fromIndex=0, xrange=xrange, len=len):
    for i in xrange(fromIndex, len(arr)):
        if arr[i] == value:
            return i
    return -1

def indexOf(arr, value, fromIndex=0):
    try:
        return arr[fromIndex:].index(value)
    except ValueError:
        return -1

def initial(arr):
    return arr[:-1]

def intersection(arr=[], *arrays):
    return list(set(arr).intersection(*arrays))

def intersectionBy():
    pass

def intersectionWith():
    pass

def join(arr, seperator=','):
    return seperator.join(arr)

def last(arr):
    return arr[-1]

def lastIndexOf():
    pass

def pull(arr, *values):
    for value in values:
        while value in arr:
            arr.remove(value)
    return arr

def pullAll(arr, values):
    return pull(arr, *values)

def pullAllBy():
    pass

def pullAllWith():
    pass

def pullAt(arr, *indexes):
    removed = []
    for shift, index in enumerate(sorted(indexes)):
        removed.append(arr.pop(index - shift))
    return removed

def remove():
    pass

def reverse(arr):
    arr.reverse()
    return arr

def slice():
    pass


    
