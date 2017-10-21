#!/usr/bin/env python

myfile = open('testfile2.txt')

for line in myfile:
	line = line.strip()
	print ">> ", line
