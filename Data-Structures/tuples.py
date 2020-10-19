
class Tuples:
    '''
        Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
        In Python dictionaries are written with normal brackets
        ()
    '''
    def tuples():
        '''
            In this example we will make a tuple of game modes
            in a game
        '''
        our_first_tuple = ("Normal","Super-crash","Hold-the-time","No-ammo" )
        #Now that we have this tuple lets see what we can do with 
        

        #accessing tuple indexes, we do this using block brackets and an index to show which index we referring to
        first_index = our_first_tuple[0]
       

        # range of indexes like how we did in lists
        first_to_third = our_first_tuple[0:2]

        '''
            Note: Tuples can not be changed,  in order to change a tuple we would need to change
            the tuple to a list then change the value and convert back to a tuple
        '''

        # joining tuples 
        second_tuple = ("Bonus-mode", "Super-powers")
        third_tuple = our_first_tuple + second_tuple
        print(third_tuple)

tester = Tuples.tuples()