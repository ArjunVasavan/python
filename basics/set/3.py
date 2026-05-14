arr = [1,2,3,4,4]

s = set(arr)

found = False

for x in arr:
    if x in s:
        print("yes it contains duplicate")
        found = True
        break;
    s.add(x)


if not found:
    print("Not found")
