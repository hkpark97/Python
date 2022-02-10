#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()




# str.strip() removes all whitespace from both the end and start of the string. In other words, it is the line.strip() method call that produces a line without the initial whitespace.

# If you wanted to remove just the newline, use str.rstrip():

# >>> '   rule match:\n'.strip()
# 'rule match:'
# >>> '   rule match:\n'.rstrip('\n')
# '   rule match:'