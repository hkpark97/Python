#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def function(n):
#     print(n)

# function(47)

# def === defines

def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False   
    else:
        return True

n = 5
if isPrime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')                     
