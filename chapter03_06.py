# 집합

a = set()
b = {1, 2, 3, 4}
e = {'foo', 'bar', 'baz', 'foo'}

# 튜플 변환
t = tuple(b)
print(t)

# 리스트 변환
li = list(b)
print(b)

# 활용
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 중복 원소 확인
print(s1.isdisjoint(s2))

# 부분 집합 확인
print(s1.issubset(s2))
print(s1.issuperset(s2))

# 추가 제거
s1 = {1, 2, 3, 4}

s1.add(5)
s1.remove(2)
print(s1)

print(s1.discard(6))  # None 예외발생 X
print(s1)

s1.clear()
print(s1)
