# 리스트
a = []
b = list()
c = [2, 3, 6, 5, 9, 8, 10]
d = [1000, 1000, 'A']
e = [d, c]

# 인덱싱
print(e[0][2])
print(e[-1][1])

# 슬라이싱
print(d[:2])

# 리스트 연산
print(c + d)

# identity
temp = c
print(id(temp), id(c))
print()

# 리스트 수정
c[0] = 4
c[1:2] = ['a', 'b', 'c']
c[1] = ['a', 'b', 'c']
print(c)

c[1:3] = []
del c[2]
print(c)
print()

# 리스트 함수
a = [5, 2, 3, 4, 6]
print(a)

a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.insert(2, 7)
print(a)
a.reverse()
print(a)
a.remove(10)
print(a)
print(a.pop())
print(a)
print(a.count(4))
ex = [8, 9]
a.extend(ex)
print(a)

li = [2, 5, 3, 5]
li.remove(5)
print(li)
