'''
Created on May 30, 2014

Illustrative example which shows how duck typing can work.
Each of the classes exhibits the duck-like behavior, while only the Not_A_Duck exhibits other expected behaviors as well.
When the function make_it_quack is executed with either class of object passed into it, they will both execute the quacking method properly.
Note that they will exhibit DIFFERENT behavior when the quacking method is executed.
When the function do_nonduck_things is executed with either class, they do not both execute properly.
The Not_A_Duck executes just fine, but Ducks do not have the expected behavior, so a runtime exception is raised.

@author: MRHardwick
'''

class Duck(object):
    
    def quacking(self):
        print "I'm quacking"

class Not_A_Duck(object):

    def quacking(self):
        print "I'm busy with other non-duck things"
        
    def doing_other_things_too(self):
        print "You've found my real purpose"
    

def make_it_quack(duck):
    duck.quacking()

def do_nonduck_things(not_a_duck):
    not_a_duck.doing_other_things_too()

if __name__ == '__main__':
    
    a_duck = Duck()
    something_else = Not_A_Duck()
    
    make_it_quack(a_duck)
    make_it_quack(something_else)
    
    do_nonduck_things(something_else)
    do_nonduck_things(a_duck)