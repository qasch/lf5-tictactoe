## import the whole random module
# import random
## when calling randint() we have to do it by using dot-notation:
# number = random.randint(1, 9)


# Best Practics:
# just import randint() method from module, not the rest
from random import randint

# when calling randint() method, we can call it directly
# without specifing modulname.method()
number = randint(1, 9)

print(number)