'''
Created on May 30, 2014

Prints all of the numbers from 1 to some input number, each on a separate line.
For all multiples of 3, Fizz is printed in its place.
For all multiples of 5, Buzz is printed in its place.
For all multiples of both 3 and 5, FizzBuzz is printed in its place.

@author: MRHardwick
'''

def get_input_number():
    """Get an input number from the standard console input.
    
    If there are any issues reading the number or converting to integer, repeat the elicitation.
    """
    
    input_integer = None
    
    # Repeatedly elicit an integer from standard console input.
    
    while input_integer == None:
        
        try:
            input_integer = int(input())
            
        except:
            print 'Please input a number..'
        
    return input_integer

if __name__ == '__main__':
    
    input_num = get_input_number()
    
    # Loop from 1 to the elicited number.
    
    for i in range(1, input_num+1):
        
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