num = [1,2,3,4,4,5,6]

num.append(30)

num.insert(0,100)

print(num)

num.insert(0,100)

print(num)

num.remove(100)

print(num)

num.pop()

print(num)

num.sort()

print(num)

num.reverse()

print(num)

another_number = num.copy()

print(another_number)

uniques = []

for nun in another_number:
    if nun not in uniques:
        uniques.append(nun)

print(uniques)

print(4 in num)

print(2929 in num)

print(num.index(2929))  # you get an error if number is not present 



