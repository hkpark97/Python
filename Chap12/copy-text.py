#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt') #read mode 
    outfile = open('lines-copy.txt', 'wt') # write mode
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

# The flush() method in Python file handling clears the internal buffer of the file. 
# In Python, files are automatically flushed while closing them. 
# However, a programmer can flush a file before closing it by using the flush() method. 


