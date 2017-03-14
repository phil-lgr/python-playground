# lists
my_list = [1, 2, 3]
print my_list
my_list = ['string', 23, 1.2, 'o']
print my_list
print len(my_list)
print my_list.__len__()
# indexes
print my_list[1:3:1]
# immutable ?
my_list[0] = 'string2'
print my_list
# concatenate
print my_list + ['a']
print my_list * 2
# append
my_list.append('x')
print my_list
# pop
print my_list.pop()
print my_list
x = my_list.pop(0)
print x
print my_list
# error if your pop undefined index
new_list = ['a', 'e', 'x', 'b', 'c']
new_list.reverse()
print new_list
# matrix
matrix = [[1,2,3],[4,5,6], [7,8,9]]
print matrix*3
# list comprehensions
first_col = [row[0] for row in matrix]
gen = [row[0] for row in matrix]
print gen
b = [1,1,[1,2]]
print b[2][1]
# short list comprehensions
print 1 in matrix[0]
