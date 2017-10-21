#!/usr/bin/env python

import sys
# import pdb

def PrintUsage():
    print "Usage: ", sys.argv[0], " <filename>\n"
    return

# Enable debugging...
#pdb.set_trace()

if( len(sys.argv) < 3 ):
    # Read the first arg passed as the filename we'll output, or default to testfile2.txt...
    try:
        filename = sys.argv[1]
    except:
        filename = 'testdata/testfile2.txt'
        

    # Open the file and print it line by line, with our prepend characters...
    try:
        myfile = open(filename)
    except IOError:
        print "Error! File", filename, "was not found or could not be read."
        PrintUsage()
        sys.exit()
    except Exception as e:
        print "Error! Caught exception [", e, "] while trying to execute. Terminating."
        PrintUsage()
        sys.exit()

    # Great success! We've opened the file. Let's print it line by line...
    for line in myfile:
	    line = line.strip()
	    print ">> ", line
else:
    PrintUsage()
    sys.exit()