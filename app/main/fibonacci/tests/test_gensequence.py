#!/usr/bin/python

# test_gensequence.py
# simple unit test for the gensequence function of the fibonacci module

from .. import gensequence

def test_gensequence():
    assert gensequence(7) == [0, 1, 1, 2, 3, 5]