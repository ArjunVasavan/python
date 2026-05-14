arr = [2, 7, 11, 15]

target = 9

mp = {}

for i in range ( len ( arr )) :
    if target - arr[i] in mp:
        print(mp[target - arr[i]],i)
    mp[arr[i]] = i
