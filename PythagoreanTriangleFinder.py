'''
Created on Apr 10, 2013

This program checks for Pythagorean Triangle Triples where x and y are less than 100 via brute force.
@author: Stanley Wong
'''
#! /usr/bin/python

# Create lists that each contain 100 elements.  
listNumX = range(1,100)
listNumY = range(1,100)
listNumZ = range(1,100)


# Brute force method to find all the Pythagorean Triples
for x in listNumX:
    for y in listNumY:
        for z in listNumZ:
            if(x*x + y*y) == (z*z):                 # X squared + Y squared = Z squared ??
                if(x<y):                            # Pythagorean Triple is printed only once to screen
                    print ("Pythagorean Triangle Triple: " ,x, y, z)
    
