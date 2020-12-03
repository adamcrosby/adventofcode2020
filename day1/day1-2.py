#!/usr/bin/env python

import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename, 'r')
    numbers = []
    for line in f:
        numbers.append(int(line))
    
    for num in numbers:
        for inner in numbers:
            #print("Trying", inner, " * ", num)
            for lol in numbers:
                if lol + num + inner == 2020:
                    print("Found: ", num, " + ", inner, "+ ", lol, " = 2020" )
                    print("answer is: ", num * inner * lol)
                    break
    

    