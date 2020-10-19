
class Sets:
    '''
        Set is a collection which is unordered and unindexed. No duplicate members.
        In Python sets are written with curly brackets, and they DO NOT have keys and values.
        Once a set is created you can not maniplulate existing data but you can add data 
        {}
    '''
    def sets():
        '''
            In this example we will make a set that will hold names
            of people that are part of a program
        '''
        our_first_set = {"j","e","l","l","o"}
        #Now that we have this set lets see what we can do with it

        #removing an value from the set
        # our_first_set.remove("Bob")

        # joining two sets using the union keyword
        second_set = {"Adriann", "Ryan"}
        third_set = our_first_set.union(second_set)
        print(our_first_set)

        #doing the same with update instead
        # third_set = our_first_set.update(second_set)
        # print(third_set)

        '''
            Note: union and update wil exclude any duplicate values
        '''

test = Sets.sets()
