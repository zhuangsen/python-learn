import time
import functools
import os
from functools import reduce
import operator


def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s in %f %s' % (f.__name__, t, unit))
            return r

        return wrapper

    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))
print(factorial.__name__)

# sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: operator.le(s1.upper(), s2.upper()))

print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

print(os.path.isdir(r'C:\Windows'))
print(os.path.isfile(r'C:\Windows\notepad.exe'))

try:
    import json
except ImportError:
    import simplejson as json
print(json.dumps({'python': 2.7}))

s = 'am I an unicode?'
print(isinstance(s, unicode))
