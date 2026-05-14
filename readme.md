# Python Roadmap for Embedded Systems Engineer
### Goal: Learn enough Python to legitimately add it to your resume

---

## Stage 1 — Basics (Week 1)
> Think of this as learning Python syntax, just like you learned C syntax

### Variables & Data Types
```python
name = "Arjun"        # string
age = 22              # integer
voltage = 3.3         # float
is_active = True      # boolean
```

### Taking Input & Printing Output
```python
name = input("Enter your name: ")
print("Hello,", name)
```

### If / Else Conditions
```python
speed = 80

if speed > 100:
    print("Overspeed!")
elif speed > 60:
    print("Normal speed")
else:
    print("Too slow")
```

### For Loop
```python
# Print numbers 0 to 4
for i in range(5):
    print(i)

# Loop over a list
sensors = ["temp", "speed", "pressure"]
for sensor in sensors:
    print(sensor)
```

### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Functions
```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 30
```

---

## Stage 2 — Data Structures (Week 1–2)
> Python has built-in lists, dicts etc. — no malloc needed!

### Lists (like arrays in C)
```python
temps = [25.1, 26.3, 24.8, 27.0]
temps.append(28.5)       # add element
print(temps[0])          # access by index
print(len(temps))        # length
```

### Dictionary (key-value pairs)
```python
device = {
    "id": 1,
    "name": "PIC18F4580",
    "baudrate": 9600
}
print(device["name"])    # PIC18F4580
```

### Tuples & Sets
```python
coords = (10, 20)        # tuple — immutable
unique_ids = {1, 2, 3}   # set — no duplicates
```

---

## Stage 3 — File I/O (Week 2)
> Very useful for reading/writing device logs

### Read a file
```python
with open("device_log.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Write to a file
```python
with open("output.txt", "w") as f:
    f.write("Speed: 80 km/h\n")
    f.write("Temp: 25.3 C\n")
```

### Read a CSV log file
```python
import csv

with open("sensor_log.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## Stage 4 — String Operations & Parsing (Week 2)
> Essential for parsing serial/device output

### String basics
```python
log = "SPEED:80 TEMP:25 STATUS:OK"

print(log.split())           # ['SPEED:80', 'TEMP:25', 'STATUS:OK']
print(log.lower())           # lowercase
print("SPEED" in log)        # True — check if substring exists
print(log.replace("OK","ERROR"))
```

### Parsing a log line (practical example)
```python
line = "SPEED:80"
key, value = line.split(":")
print(key)    # SPEED
print(value)  # 80
```

---

## Stage 5 — Modules & Error Handling (Week 3)
> This is where Python becomes useful for embedded tooling

### Importing modules
```python
import os
import sys
import time
```

### Try / Except (like error handling in C)
```python
try:
    value = int(input("Enter a number: "))
    print(10 / value)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("That's not a number")
```

### time module
```python
import time

print("Starting...")
time.sleep(2)        # wait 2 seconds
print("Done!")
```

---

## Stage 6 — Serial Communication with pyserial (Week 3)
> This is THE most useful Python skill for embedded engineers

### Install
```bash
pip install pyserial
```

### Read data from a serial port (UART)
```python
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print("Received:", line)
    time.sleep(0.1)

ser.close()
```

### Send a command over serial
```python
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.write(b'GET_SPEED\n')    # send command
response = ser.readline()
print(response.decode())
ser.close()
```

---

## Stage 7 — OOP Basics (Week 3–4)
> You already know C++ OOP, Python OOP is simpler

```python
class Sensor:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

    def read(self):
        # simulate reading
        return 25.3

temp_sensor = Sensor("Temperature", 5)
print(temp_sensor.name)
print(temp_sensor.read())
```

---

## Mini Project Ideas (Pick 1 to put on GitHub)

| Project | What it shows |
|---|---|
| Serial Log Reader | Read UART data, parse it, save to CSV |
| Device Log Analyzer | Read a .txt log, extract errors, print summary |
| Sensor Data Plotter | Read CSV data and plot with matplotlib |
| Auto Test Script | Send commands over serial, verify responses |

> **Tip:** Even one small working project on GitHub is enough to confidently say Python on your resume.

---

## What to Write on Your Resume

```
Languages: C, C++, Python (Scripting)
```
or
```
Languages: C, C++ | Scripting: Python
```

Never write just "Python" without a qualifier as a fresher — adding "Scripting" is honest and sets correct expectations.

---

## Rough Timeline

| Week | Focus |
|---|---|
| Week 1 | Stage 1 + Stage 2 (syntax, loops, data structures) |
| Week 2 | Stage 3 + Stage 4 (file I/O, string parsing) |
| Week 3 | Stage 5 + Stage 6 (modules, pyserial) |
| Week 4 | Build 1 mini project and push to GitHub |

**Total: ~4 weeks of 1–2 hours/day**

---

*Tailored for Arjun Vasavan — Embedded Systems Engineer*
