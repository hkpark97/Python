#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     kitten()

# def kitten():
#     print('Meow.')

# if __name__ == '__main__': main()

# if calls main
# __name__ will return the name of the current module
# if somebody had typed import and the name of this file, this will be running as a module
# __name__ would have the name of the module(__main__)

def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print("Meow.")
    return dict(x = 42, y = 43, z =44)

if __name__ == '__main__': main()        


# if there's no return value, the result will be print out None value
