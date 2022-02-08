#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending

# The flush() method in Python file handling clears the internal buffer of the file. 
# In Python, files are automatically flushed while closing them. 
# However, a programmer can flush a file before closing it by using the flush() method. 
# Buffer - The space that temporarily stores the data, while transmitting the data to one another, 