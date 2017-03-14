# string single quote
print 'hello'
print "hello" + 'world'
print "'hello'"
print '"hello"'
# newline
print 'hello \n fasdfa \t tab'
# length of string
print len('hello')
print 'hello'.__len__()
'hello'.__len__()
# accessor
s = 'hello'
print s[1:]
print  s[-1]
print s[:-1]
#  frequency
print s[::1]
print s[::2]
print s[::-1]
# [start:end:interval]

# strings are immutable
s = 'hello world'
# can't do s[0]
print s + 'phil'
# reasign
s = s + 'phil'
print s
# multiply
print s*10
# string methods
print s.upper()
print s.lower()
print s.split('')
print s.split()


