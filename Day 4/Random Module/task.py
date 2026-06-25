import random
#import my_module

#How to create random generating #'s (Different #'s everytime you run the code.)
#random_integer = random.randint(1, 10)
#print(random_integer)

#Using my_module
#print(my_module.my_favorite_number)

#Using the random module                     # VERY IMPORTANT!!!
#random_number_0_to_1 = random.random() * 10 # <-Some functions take arguments, however not all functions take arg
#print(random_number_0_to_1)                 # Some just need empty parenthesis to become activated ()

#random_float = random.uniform(1, 10)
#print(random_float)

#Heads or Tails
random_pick = random.randint(0, 1)

if random_pick == 0:
    print("Heads!")
else:
    print("Tails!")
