#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     print('Hello, World.')

# if __name__ == '__main__': main()


class Car:
    model = 'Ford'
    def print_model(self):
        print(self.model)

myCar = Car()
myCar.print_model()      

# self is refering to myCar
