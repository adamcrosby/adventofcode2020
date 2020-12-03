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
            if num + inner == 2020:
                print("Found: ", num, " * ", inner, " = 2020" )
                print("answer is: ", num * inner)
                break
    

    