# range and xrange
for i in range(0, 10) + ['end']:  # range are saved in memory
    print "{i} is of type {type}".format(i=i, type=type(i))

list = [xrange(0, 5)] + ['end']

print type(list[0])
print list

# range is not saved in memory, good for big range in v2
for a in list:
    for b in a:
        print "{i} is of type {type}".format(i=b, type=type(b))

# deconstructing a xrange
for a, b, c in [xrange(0, 3)]:
    print [a, b, c]

print [x for x in xrange(0,3)]

for a in xrange(0, 3):
    print [a, b, c]

print range(0, 3)

# print type(xrange(0, 10))
# print type(range(0, 10))
