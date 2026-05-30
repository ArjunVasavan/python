# =============================================================================
# DECORATORS 
# =============================================================================
import functools
import time


# =============================================================================
# 1. THE CONCEPT
# =============================================================================
# A decorator wraps a function with extra behaviour.
# @decorator is just shorthand for: func = decorator(func)
#
# Template — copy this every time you write a decorator:
#
#   def my_decorator(func):
#       @functools.wraps(func)        # always include this
#       def wrapper(*args, **kwargs):
#           # --- before ---
#           result = func(*args, **kwargs)
#           # --- after ---
#           return result
#       return wrapper


# =============================================================================
# 2. TIMER — how long does this function take? (profiling, performance)
# =============================================================================
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"[TIMER] {func.__name__}() → {end - start:.4f}s")
        return result
    return wrapper

@timer
def parse_hex_file(path):
    time.sleep(0.1)   # simulate work
    return "parsed"

parse_hex_file("firmware.hex")
# [TIMER] parse_hex_file() → 0.1001s


# =============================================================================
# 3. RETRY — unstable hardware / serial / network calls
# =============================================================================
def retry(times=3, delay=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[RETRY] attempt {attempt}/{times} failed: {e}")
                    time.sleep(delay)
            raise RuntimeError(f"{func.__name__} failed after {times} retries")
        return wrapper
    return decorator

@retry(times=3, delay=0.2)
def read_uart():
    import random
    if random.random() < 0.6:
        raise IOError("UART read timeout")
    return b'\xDE\xAD\xBE\xEF'

try:
    data = read_uart()
    print(f"[UART] received: {data.hex()}")
except RuntimeError as e:
    print(e)


# =============================================================================
# 4. LOGGER — trace function calls during debugging
# =============================================================================
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result!r}")
        return result
    return wrapper

@logger
def crc8(data: bytes) -> int:
    crc = 0
    for byte in data:
        crc ^= byte
    return crc

crc8(b'\x01\x02\x03')
# [LOG] calling crc8(b'\x01\x02\x03',)
# [LOG] crc8 returned 0


# =============================================================================
# 5. VALIDATE INPUT — catch bad args before they hit hardware
# =============================================================================
def validate_gpio_pin(func):
    @functools.wraps(func)
    def wrapper(pin, *args, **kwargs):
        if not (0 <= pin <= 53):          # RPi has GPIO 0-53
            raise ValueError(f"Invalid GPIO pin: {pin}")
        return func(pin, *args, **kwargs)
    return wrapper

@validate_gpio_pin
def set_pin_high(pin):
    print(f"GPIO {pin} → HIGH")

set_pin_high(17)    # GPIO 17 → HIGH
set_pin_high(99)    # ValueError: Invalid GPIO pin: 99
