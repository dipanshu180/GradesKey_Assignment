
'''3)
Return vs Yield
Write a function which generates 100 random numbers. Use both return and yield, explain
what you observe ?'''

#Using retrun
import random

def random_return():
    ran = [random.randint(1, 100) for _ in range(100)]
    return ran

numbers = random_return()
print(numbers)

#Using yield

def random_yield():
    for _ in range(100):
        yield random.randint(1, 100)

random_generator = random_yield()
for number in random_generator:
    print(number)

"""#**Random:-** iterate the data at once
#**Yield:-** Itereate data data one by one
"""
