'''
Created on May 30, 2014

Prints all of the numbers from 1 to 107, each on a separate line, without taking input.
For all multiples of 3, Fizz is printed in its place.
For all multiples of 5, Buzz is printed in its place.
For all multiples of both 3 and 5, FizzBuzz is printed in its place.

@author: MRHardwick
'''

if __name__ == '__main__':
    
    # Loop from 1 to 107.
    
    for i in range(1, 108):
        
        # Is this number a multiple of both 3 and 5?
        
        if i % 5 == 0 and i % 3 == 0:
            print 'FizzBuzz'
            
        # Is this number a multiple of only 3?
        
        elif i % 3 == 0:
            print 'Fizz'
        
        # Is this number a multiple of only 5?
        
        elif i % 5 == 0:
            print 'Buzz'
        
        # Is this number neither a multiple of 3 or 5?
        
        elif i % 5 != 0 and i % 3 != 0:
            print i
            