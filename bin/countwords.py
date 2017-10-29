#!/usr/bin/env python

import sys
from collections import defaultdict
import string
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

    # Great success! We've opened the file. Let's count the letters and words in the file...
    letters = defaultdict(int)
    count_letters = 0
    #words = {}
    count_words = 0

    # Sweep the file letter by letter...
    for line in myfile:
        line = line.strip()
        for char in line:
            # Increment the global count of letters...
            count_letters += 1
            # Add to the count of that specific letter...
            letters[char.lower()] += 1

	# Print some useful output...
    print "\nThere were ", count_letters, "characters in the file ", filename, "\n"
    for c in string.ascii_lowercase:
        print "[", c, "] ==> ", letters[c]
else:
    PrintUsage()
    sys.exit()
