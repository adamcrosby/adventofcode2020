#!/usr/bin/env python

import sys
import re

#1-3 a: abcde
#1-3 b: cdefg
#2-9 c: ccccccccc


if __name__ == '__main__':
    f = open(sys.argv[1])
    passwords = []
    for p in f:
        passwordEntry = {'min': p.split(' ')[0].split('-')[0], 
                    'max': p.split(' ')[0].split('-')[1],
                    'letter': p.split(' ')[1][0], 
                    'string': p.split(' ')[2].rstrip()
                    }
        passwords.append(passwordEntry)

    matches = 0
    mismatches = 0
    for password in passwords:
        lettercount = password['string'].count((password['letter']))
        if (lettercount >= int(password['min'])) and (lettercount <= int(password['max'])):
            matches = matches + 1
        else:
            mismatches = mismatches + 1
    
    print("Found " + str(matches) + " matches")
    print("Found " + str(mismatches) + " mismatches")
    print("Total: " + str(matches + mismatches) + " checked")