#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

# for pet in animals:
#     print(pet)

animals = ( 'cow', 'bear', 'wolf', 'dog', 'chicken' )

for pet in animals:
    if pet == 'cow': continue #skip printing out the cow
    # if pet == 'chicken': break
    print(pet)
else:
    print("That is all of the animals")    


# uses sequence(item)
