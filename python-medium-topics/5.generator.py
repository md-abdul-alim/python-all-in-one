# https://www.youtube.com/watch?v=4ly-auU-OMA
# https://www.youtube.com/watch?v=Uo8_8VNY2nk

# https://www.youtube.com/watch?v=mziIj4M_uwk
# return terminate the function
# yield doesn't terminate the function

"""
generator is a special type of iterable. which iterate items without storing them all in memory at once.
This is used to optimize memory usage and improve performance.
The yield keyword use to return values one at a time when the generator is iterated.
yield return a generator object at a time
generator doesn't generate and store all the items in memory at once.
generator can be used to control the iteration behaviour of a loop. A generator is very similar to function that
returns an array.
"""


def number_generator(num):
    for i in range(num):
        yield i


gen = number_generator(5)
print(gen)
for num in gen:
    print(num)


def generator_function():
    yield 1
    yield 2
    yield 3


gen = generator_function()

for val in gen:
    print(val)