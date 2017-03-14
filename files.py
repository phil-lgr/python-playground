# file
f = open('text.txt')
print f.read()
f.seek(0)
print f.read()
f.seek(0)
# readlines saves the file in memory
print f.readlines()
print f.read()
# write
my_file = open('test1.txt','w+') # mode
my_file.write('This is a new line')
my_file.close()
# for loop
for line in open('text.txt'):
    print line
