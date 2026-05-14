s = set()

s.add(1)
s.add(2)
s.add(2)
s.add(1)
s.add(1)
s.add(1)
s.add(4)
s.add(4)
s.add(2)
s.add(2)
s.add(2)
s.add(2)
s.add(2)
s.add(2)
s.add(3)
s.add(3)
s.add(3)
s.add(3)
s.add(3)
s.add(3)
s.add(3)
s.add(3)
s.add(2)
s.add(2)
s.add(2)
s.add(3)
s.add(4)

if 1 in s:
    print("yes")

for x in s:
    print(x)

s.remove(3)

print(s)
