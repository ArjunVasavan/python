# =============================================================================
# GENERATORS - BASICS
# A generator function uses `yield` instead of `return`
# Python auto-creates __iter__ and __next__ for you
# =============================================================================

# --- SIMPLE GENERATOR ---
def count_up(start, stop):
    while start < stop:
        yield start       # suspends here, saves state, returns value
        start += 1        # resumes from here on next next() call

gen = count_up(0, 5)
print(type(gen))          # <class 'generator'>
print(next(gen))          # 0
print(next(gen))          # 1

for n in count_up(0, 5):
    print(n)              # 0 1 2 3 4


# --- WHY GENERATORS? LAZY EVALUATION ---
# Values produced ONE AT A TIME, not all stored in memory

def infinite_counter(start=0):
    while True:
        yield start
        start += 1

counter = infinite_counter()
print(next(counter))   # 0
print(next(counter))   # 1
print(next(counter))   # 2
# This would run forever but never crash on memory


# --- GENERATOR EXPRESSION (like list comp but lazy) ---
squares_list = [x**2 for x in range(10)]    # entire list in memory
squares_gen  = (x**2 for x in range(10))    # one value at a time

print(next(squares_gen))   # 0
print(next(squares_gen))   # 1

# Memory comparison:
import sys
print(sys.getsizeof(squares_list))   # ~184 bytes
print(sys.getsizeof(squares_gen))    # ~200 bytes (but scales to millions cheaply)
