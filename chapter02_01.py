import sys

print('Python start!')

# separator

print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('id', 'example.com', sep='@')

# end

print('welcome to', end=' ')
print('ukraine news', end=' ')
print('website')

print('learn python', file=sys.stdout)
print()

d = 3
s = 'python'
f = 3.1445454

print('%d %s %.7f' % (d, s, f))
print('{} {} {}'.format(d, s, f))
print('{2} {1} {0}'.format(d, s, f))

# %s

print('%10s' % "nice")
print('{:>10}'.format('nice'))

print('%-10s' % "nice")
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:$>10}'.format('nice'))

print('%.5s' % 'python day')
print('{:10.5}'.format('python day'))

# %d

print("%d %d" % (1, 2))
print(' {} {}'.format(1, 2))

print('%4d' % 42)
print('{:4d}'.format(42))

# %f

print('%f' % 3.151515481868796)
print('{:f}'.format(3.151515481868796))

print('%06.2f' % 3.151515481868796)
print('{:06.2f}'.format(3.151515481868796))
