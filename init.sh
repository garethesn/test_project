#!/bin/bash

# This sets up some test data for use with the repo...
TESTFILE3_URL='http://www.gutenberg.org/files/2600/2600-0.txt'
curl "${TESTFILE3_URL}" -o testdata/testfile3.txt
