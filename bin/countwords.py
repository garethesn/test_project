#!/usr/bin/env python

import sys
import string
# import pdb


def PrintUsage():
    print "Usage: ", sys.argv[0], " <filename>\n"
    return

# Enable debugging...
# pdb.set_trace()


if(len(sys.argv) < 3):
    # Read the first arg passed as the filename we'll output, or default to
    # testfile2.txt...
    try:
        filename = sys.argv[1]
    except Exception as e:
        filename = 'testdata/testfile2.txt'

    # Open the file and print it line by line, with our prepend characters...
    try:
        myfile = open(filename)
    except IOError:
        print "Error! File", filename, "was not found or could not be read."
        PrintUsage()
        sys.exit()
    except Exception as e:
        print "Error! Caught exception [", e,\
            "] while trying to execute. Terminating."
        PrintUsage()
        sys.exit()

    # Great success! We've opened the file. Let's count the letters and words
    # in the file...
    word = ''
    words = {}
    count_words = 0

    # Sweep the file letter by letter...
    for line in myfile:
        line = line.strip()
        for char in line:
            # pdb.set_trace()
            if(char in string.punctuation or char in string.whitespace):
                # Word is complete. File it...
                if(len(word) > 0):
                    count_words += 1
                    if(word in words):
                        words[word] += 1
                    else:
                        words[word] = 1
                word = ''
            else:
                # Add the character to the word and continue...
                word += char.lower()

    # Print some useful output...
    print "\nThere were ", count_words, "words in the file ", filename, "\n"
    # Show the most frequently occurring words first...
    for key, value in reversed(
            sorted(words.iteritems(), key=lambda (k, v): (v, k))):
        print "[", key, "] ==> ", value
    # for w in words:
    #    print "[", w, "] ==> ", words[w]
else:
    PrintUsage()
    sys.exit()
