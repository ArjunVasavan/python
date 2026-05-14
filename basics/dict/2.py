arr = [1, 1, 2, 3, 3, 3]

mp = {}

for x in arr:
    mp[x] = mp.get(x,0) + 1;

print(mp)
