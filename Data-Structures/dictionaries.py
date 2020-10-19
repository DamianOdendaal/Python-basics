

class Dictionaries:
    '''
        A dictionary is a collection which is unordered, changeable and indexed data. You also cant have duplicate values 
        In Python dictionaries are written with curly brackets, and they have keys and values.
        {"key":"value"}
    '''
    #JSON --> Javascript Object notation
    def dicts():
        '''
            In this example we will make a person dictionary holding 
            data that would describe a person
        '''
        our_first_dictionary = {
            "age": 21,
            "name": "Jonathan",
            "favourite_sport": "Rugby",
            "second_name": "",
            "some_first_pet_dog": "johnny",
            "some_first_pet_cat": "flluff",
            "some_dirt": "brown"
        }
        # hey = "damian"
        # print(type(hey))
        #accessing keys within a dictionary ,  Which way here would be a better practice?
        user_name = our_first_dictionary.get("namee")
        user_name = our_first_dictionary["name"]
        #since dicts have key:value pairs we can get all the keys or all values from a dictionary using
        keys = our_first_dictionary.keys()
        values = our_first_dictionary.values()
        # print(f"this adds some weird stuff {keys}, {values}")
        #if we want to update values in a dictionary 
        # left:right
        our_first_dictionary["second_name1w"] = "March"
        print(our_first_dictionary)
        our_first_copied_dict = dict(our_first_dictionary)


        # They can be nested within each other

        #parent
        myfamily = {

            "0" : {
              "name" : "Emil",
              "birth_year" : 2004
            },

            "1" : {
              "name" : "Tobias",
              "birth_year" : 2007
            },

            "2" : {
              "name" : "Linus",
              "birth_year" : 2011
            }
        }



        # index = 0
        # while index < 3:
        #     names = myfamily[str(index)]["name"]
        #     # print(names)
        #     birth_years = myfamily[str(index)]["birth_year"]
        #     print(birth_years)
        #     index += 1



test = Dictionaries.dicts()




