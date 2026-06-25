import random
#Creating a list
states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana"]

#if I wanted to rename something in the list, it'll go like this:
states_of_america[1] = "AlaBammah"
#print(states_of_america)

#When creating a list, must use square brackets[]
#To extract from the list, use square brackets as well []

#Adding to the end of list use the -> .append() remember the parenthesis activates the function
#states_of_america.append("Seven's Asylum")
#print(states_of_america)

#Extending a list
states_of_america.extend(["LOL Land", "Waterfalls"])
print(states_of_america)