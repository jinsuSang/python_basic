# while

a = ['a', 'b', 'c']

while a:
    print(a.pop())

a = ['a', 'b', 'c']
s = 'd'

i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print('not found')
