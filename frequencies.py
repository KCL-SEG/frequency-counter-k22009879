"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections


def frequencies(items):
    newlist = []
    for item in items:
        item = str(item)
        newlist.append(item)
    
    counter = collections.Counter(newlist)

    frequencies = dict(counter)
    print(frequencies)

    # Your code goes here
    return frequencies


