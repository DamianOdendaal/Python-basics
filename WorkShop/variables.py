'''
    In python a variable is a container used to store data

    Where the data comes from matters very little
    


'''

#example 1
x = 5
y = "John"
print(x)
print(y)


#example 2 (declaring more than one variable on a line)
x,y = 1,2
print(x)
print(y)


#example 3 (data from a function call)
def give_data_to_me():
    return "data"

test = give_data_to_me()
print(test)

#example 3 (data extracted from a data structure)

lis = [1, 2, 3, 4, 5]
no_first_and_last = lis[1:-1]
print(no_first_and_last)