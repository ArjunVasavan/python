arr = [1,2,3,2]

s = set()

for x in arr:
    if x in s:
        print("duplicate found")
    s.add(x)
