f = open('text.txt')

char = f.read(1)

while char != 'o':
    print char

    char = f.read(1)

print char

x = 1

while False:
    x += 1
    print x
    if x == 9:
        break # go to beginning of while
        print 'was 9'
    else:
        print 'hello'
    print 'dabana'  # skipped for x == 9
else:
    print 'while was completed'
