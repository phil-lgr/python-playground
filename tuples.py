# tuples
t = (1,2,3)
print t[0]
print t.count('')
# dic.items outputs a list of tuples
dic = {
    'name': 'phil',
    'last': 'leger',
    1: 23,
    1: 24
}
print dic.items()[0][0]
# immutable
t[0] = 2
