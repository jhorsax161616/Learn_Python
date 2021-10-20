def make_multiplier(x):

    def multiplier(n):
        return x * n
    
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(4))
print(times4(3))
print(times4(times10(2)))