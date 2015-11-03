# -*- coding: utf-8 -*-
print 'Hello world'
x=50
for i in range(x):
	print i,

a=range(10)
print a
print ' '.join([str(x) for x in a])
if x>5:
	print 'è maggiore'

x**=x
print x
