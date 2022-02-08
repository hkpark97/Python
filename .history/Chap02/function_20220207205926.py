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

def list_prime():
    for n in range(100): #range from 0 to 100, not including 100
        if isPrime(n):
            print(n, end='  ', flush=True) #end='  ' => gives space beteween two words        

n = 1
if isPrime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')                     
