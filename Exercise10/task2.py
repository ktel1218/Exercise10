#!/bin/env python

"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""
d = {"q": 5, "m": 3, "z":2, "a": 10}

keys = []
for key in d:
    keys.append(key)

sorted_keys = sorted(keys)

for item in sorted_keys:
    print "%s, %r"%(item, d[item])