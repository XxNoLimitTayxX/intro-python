
# 1. In your own words, describe what a function is
'A function is a reueable command or set of instructions.'

# 2. What is are function parameters and arguments and describe
# the difference between the 2.
'A function parameter is variable defined already for us while an argument supports something like data.'

# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
from sklearn import impute


userName = "Tay Bridges"

print("Welcome " + userName + ' to the matrix!')

# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)


def calculate(randNumber1, randNumber2, randNumber3):

    print(randNumber1 + randNumber2 + randNumber3)


calculate(7, 100, 700)

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data


def userMsg(nextClass):
    nextClass = imput('what is your next class. ')
    print("Greetings! You have another class which is" + nextClass + "!")


userMsg()
