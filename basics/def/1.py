def get_odds(arr):
    ans = []

    for x in arr:
        if x % 2 != 0:
            ans.append(x)

    return ans


# example call
arr = [1,2,3,4,5]
print(get_odds(arr))
