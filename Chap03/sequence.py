#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]
# x[0] = 12 #assign to specific index value
# for i in x:
#     print('i is {}'.format(i))
    


# # x = range(10) # starts from 0 to 9
# x = range(5, 50, 5) #stars from 5 to 49 step by 5
# for i in x:
#     print('i is {}'.format(i))


x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))