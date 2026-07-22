#Function in python
#Functions act as isolated blocks of reusable code designed to complete specific tasks cleanly. Use the def keyword to build them.

def greet_user(user):                    #making a function with a parameter 'user'
    return "Welcome, " + user + "!"      #returning a string that greets the user with their name

#calling the function
user = input("Enter your name: ")        #EX:input: om
message = greet_user(user)               #calling the function and storing the return value in a variable
print(message)                           #output: Welcome, om!
