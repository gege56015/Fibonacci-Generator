#!/usr/bin/python

# gensequence.py
# contains a function for generating a fibonacci sequence

def gensequence(end):
	sequence = [0,1]
	while True:
		currentnumber = sequence[-2:][0] + sequence[-2:][1]
		if currentnumber >= end:
			return sequence
			break
		else:
			sequence.append(currentnumber)


