'''

Local (or function) scope is the code block or body of any Python function or lambda expression.
This Python scope contains the names that you define inside the function. These names will only be visible from the code of the function.
It’s created at function call, not at function definition, so you’ll have as many different local scopes as function calls. 
This is true even if you call the same function multiple times, or recursively. Each call will result in a new local scope being created.

'''


'''
Enclosing (or nonlocal) scope is a special scope that only exists for nested functions.
If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function.
This scope contains the names that you define in the enclosing function.
The names in the enclosing scope are visible from the code of the inner and enclosing functions.

'''

'''
Global (or module) scope is the top-most scope in a Python program, script, or module.
This Python scope contains all of the names that you define at the top level of a program or a module. 
Names in this Python scope are visible from everywhere in your code.

'''

'''
Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session.
This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python.
Names in this Python scope are also available from everywhere in your code. It’s automatically loaded by Python when you run a program or script.

'''

my_name = "Damian111"

class Scope:
    '''
        Python scope can be a little confusing at first but we can make it simpler by understanding 
        the different scopes we have and what they are used for 
    '''
    def local_scope():
        '''
            When we refer to something as a local variable it means you can only 
            make use of it where you created it. This variable will be usable where
            it was created and only there. Like a variable that can only be used in this function
        '''
        #a variable that can only be used in the local scope method
        local_var = 0
        print(local_var)
        local_var = 6


    def global_scope():
        '''
            Global (or module) scope is the top-most scope in a Python program, script, or module.
            This Python scope contains all of the names that you define at the top level of a program or a module.
            Names in this Python scope are visible from everywhere in your code.
        '''
        
        new_variable = my_name
        print(new_variable)

    #test if microwave is hot enough
    #parent function
    def enclosing_scope(take_in_data):
        '''
            Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. 
            If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function.
        '''
        temp = "750'"

        #child function
        def actual_enclosing_scope(take_in_data):
            print(temp, take_in_data)

        #look how we had to first call the function even though we defined if here in this specific function
        actual_enclosing_scope()





    def built_in_scope():
        '''
            Calling a built in scope method is when we call methods that 
            are built in to python for example the famous print 
        '''
        print("hello world")


test = Scope.local_scope()
test = Scope.global_scope()