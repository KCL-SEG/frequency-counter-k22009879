"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections


def frequencies(items):
    for item in items:
        str(item)
    counter = collections.Counter(items)

    frequencies = dict(counter)

    # Your code goes here
    return frequencies
