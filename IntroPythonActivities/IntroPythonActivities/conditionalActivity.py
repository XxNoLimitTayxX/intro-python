# 1. What is the difference between 
# a parameter and an argument in a python function
"A paramater is a data holder while an argument is the data."

# 2. In your own words, describe what 
# a conditional statement (if/else) is 
"If/Else is a function that depends on IF something is true and if it is anything else, it would do another thing."

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )

moneyOnCard = 262.22
costOfItem = 189

if moneyOnCard > costOfItem:
    print("Thank you for your purchase!")
else:print("Sorry, insufficient funds. Please try again or enter another payment option.")


# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

def foodInFridge():
    foodInFridge = False

if foodInFridge == True:
    print("Time to cook!")
else:print("Time to Shop!")


# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".