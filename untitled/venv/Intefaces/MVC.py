def divide(x,y):
    return x/y

def divisor(d):
    return lambda x: divide(x,d)

half = divisor(2)
third = divisor(3)

print(half(14),third(27))
