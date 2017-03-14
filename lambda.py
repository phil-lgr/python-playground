# lamda expression are meant to be used for "small"

def square(num):
    return num ** 2


l_square = lambda num: num ** 2
print l_square(2)

rev = lambda s: s[::-1]
print rev([1, 2])

adder = lambda (s, d): s + d
print adder(1,2)


