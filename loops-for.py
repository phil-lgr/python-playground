# iterator: lists, tuples, sets
l = [1, 2, 3, 4, 5, 6]

for item in l:
    if item % 2 == 0:
        print 'number {x} is odd'.format(x=item.__str__())
    else:
        print 'number {x} is even'.format(x=item.__str__())

list_sum = 0

for num in l:
    list_sum += num

print list_sum

for char in 'hello':
    print char.upper()

tup = (1, 2, 3, 4, 5, 6)

for item in tup:
    print item

list1 = [(2, 4), (6, 8)]

for tup in list1:
    print tup

# tuple unpacking
for (t1, t2) in list1:
    print t1
    print t2

d = {
    'a': 1,
    'b': 2,
    'c': 3
}

for (key, value) in d.items():
    print "Key is {key}, value is {value}".format(key=key, value=value)

list2 = [(1, 2, 3), (4, 5, 6)]
list3 = [[1, 2, 3], [4, 5, 6]]

for (v1, v2, v3) in list2:
    print "{v1}, {v2}, {v3}".format(v1=v1, v2=v2, v3=v3)

for [v1, v2, v3] in list3:
    print "{v1}, {v2}, {v3}".format(v1=v1, v2=v2, v3=v3)
