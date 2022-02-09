#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     print('Hello, World.')
    

# Handling exceptions
def main():
    try:
        x = int('foo')
    except ValueError:
        print('I caught a ValueError')    

if __name__ == '__main__': main()
