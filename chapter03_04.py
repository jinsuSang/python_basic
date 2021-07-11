# 튜플
# 리스트와 비교
# 수정 및 삭제 불가
# immutable

a = ()
b = (1,)
c = tuple([5, 6, 7, 8, 9, 10])
d = (1000, 100000, ('clover',))

print(d[0])
print(d[-1])
print(d[:2])

# 튜플 연산
print(c + d)
print(c * 3)

# 튜플 함수
a = (5, 6, 8, 2, 3, 1)
print(a.index(2))
print(a.count(2))

# 팩킹
t1 = ('foo', 'bar', 'bax')

# 언팩킹
(x1, x2, x3) = t1


# 팩킹과 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4 = t3
