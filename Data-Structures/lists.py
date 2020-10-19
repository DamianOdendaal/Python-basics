class Lists:
    '''
        List is a collection which is ordered and changeable. Lists also allows duplicate members.
        In Python dictionaries are written with block brackets
        []
    '''
    def lists():
        '''
            In this example we will make a list holding scores
            on a test that learners have written out of 10
        '''
        our_first_list = [7, 5, 10, 4, 6, 3]
        #Now that we have this list lets see what we can do with it

        #accessing indexes within a list, doing this we specify which index we want inside block brackets
        third_index = our_first_list[2]

        #adding new values to a list 
        our_first_list.append("hey there")


        # negative indexing 
        '''
            Note: what this means is instead of starting from the first index we rather start from the end
            so -1 refers to the last item and -2 would refer to the second last item in a list
        '''
        last_index = our_first_list[-1]
        print(last_index)


        #we can also refer to a specific range inside a list
        second_to_sixth_value = our_first_list[2:5]

      

test = Lists.lists()
