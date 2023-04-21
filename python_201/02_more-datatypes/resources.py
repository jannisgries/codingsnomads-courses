# This code snippet produces a list of random length
# filled with random numbers between 1 and 100.
# You can use it to quickly generate a random list to use in other labs
# To use it in a different script file, you can import
# the `starter` list with the following command
#
# from randlist import starter
#
# Give it a try in one of your labs!
# P.S.: There's nothing else to do in here ;)

import random

list_length = random.randint(1, 20)
randlist = list()
for i in range(list_length):
    randlist.append(random.randint(1, 100))
