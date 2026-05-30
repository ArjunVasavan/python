# =============================================================================
# GENERATORS - ADVANCED
# yield from, send(), chaining generators
# =============================================================================

# --- yield from: delegate to sub-generator ---
def inner():
    yield 1
    yield 2

def outer():
    yield 0
    yield from inner()   # flattens inner generator into outer
    yield 3

for x in outer():
    print(x)    # 0 1 2 3


# --- send(): pass values INTO a generator ---
# gen.send(val) resumes generator AND sends val as result of yield expression

def accumulator():
    total = 0
    while True:
        value = yield total    # yield sends total OUT, receives value IN
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)          # prime the generator (run until first yield)
print(acc.send(10))   # 10
print(acc.send(20))   # 30
print(acc.send(5))    # 35


# --- GENERATOR PIPELINE ---
# Chain generators like unix pipes: source | filter | transform

def read_numbers(n):
    """source: generate numbers 0..n"""
    for i in range(n):
        yield i

def only_even(nums):
    """filter: pass through only even numbers"""
    for n in nums:
        if n % 2 == 0:
            yield n

def square(nums):
    """transform: square each number"""
    for n in nums:
        yield n ** 2

# Pipeline: range -> even filter -> square
pipeline = square(only_even(read_numbers(10)))

for val in pipeline:
    print(val)    # 0 4 16 36 64  (squares of even numbers 0-8)
