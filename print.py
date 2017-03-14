
# templating
s = 'hello'
n = 13.13
print 'place s here: %s %s' %(s, n)

# float
print 'Floating point number: %1.2f' %(13.145)
# 5 char total, 4 precision point, whitespace are used to fill
print 'Floating point number: %5.4f' %(13.145)
# r formatting
print 'Convert to string %r' %(123)
# format metho
print 'First: {x} Second: {y}'.format(x='1', y='2')
