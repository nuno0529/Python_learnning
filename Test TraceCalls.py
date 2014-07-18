#!/usr/bin/python
# -*- coding: utf-8 -*-

from TraceCalls import TraceCalls

@TraceCalls(indent_step=4, show_ret=True)
def fibonacci(x):
    if x in (0, 1):
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)

# main
print 'f(%d): %d' % (4, fibonacci(4))
