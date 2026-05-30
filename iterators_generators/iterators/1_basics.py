# =============================================================================
# ITERATORS - BASICS
# =============================================================================

# --- ITERABLE vs ITERATOR ---
# Iterable: has __iter__() -> list, str, tuple, dict
# Iterator: has __iter__() AND __next__() -> returned by iter()

nums = [10, 20, 30]

it = iter(nums)       # calls nums.__iter__(), gives iterator object
print(next(it))       # 10  -> calls it.__next__()
print(next(it))       # 20
print(next(it))       # 30
# next(it)            # StopIteration -> list exhausted


# --- FOR LOOP IS JUST THIS UNDER THE HOOD ---
fruits = ["apple", "banana", "cherry"]

_iter = iter(fruits)
while True:
    try:
        fruit = next(_iter)
        print(fruit)
    except StopIteration:
        break


# --- CHECKING IF OBJECT IS ITERABLE OR ITERATOR ---
my_list = [1, 2, 3]
print(hasattr(my_list, '__iter__'))   # True  -> iterable
print(hasattr(my_list, '__next__'))   # False -> NOT an iterator

my_iter = iter(my_list)
print(hasattr(my_iter, '__next__'))   # True  -> iterator


# --- ITERATOR IS SINGLE USE ---
it2 = iter([1, 2, 3])
for x in it2: print(x)   # prints 1 2 3
for x in it2: print(x)   # prints NOTHING -> exhausted
