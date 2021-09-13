def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]

def two_sum2(numbers, target):
    d = {}
    for i,n in enumerate(numbers):
        if target-n in d:
            return [d[target-n],i]
        d[n] = i
        print(d)
print(two_sum2([1,2,3], 4))
print(two_sum2([1234,5678,9012], 14690))
print(two_sum2([2,2,3], 4))
