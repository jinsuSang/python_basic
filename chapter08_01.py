# 파이썬 내장 함수

# 절대값 abs()

print(abs(-3))

# all, any iterable 요소 검사 참 혹은 거짓
print(all([1, 2, '']))  # and
print(any([0, 0, 1]))  # or

# chr: 아스키 코드 -> 문자, ord : 문자  -> 아스키
print(chr(97))
print(ord('c'))

# enumerate : 인덱스 + Iterable 객체 생성

for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)


# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, 2, 3, 4, 5, 1, -5, -6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 3, 4, 5, 1, -5, -6])))

# id: 객체의 주소값 반환
print(id(int(5)))
print(id(4))

# len: 요소의 길이 반환
print(len('adsfsdf'))
print(len([1, -3, 2, 3, 4, 5, 1, -5, -6]))

# max, min 최대값, 최소값
print(max(1, 2, 3))
print(max('python study'))


# map : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, 3, 5, 8, -3, -8, -9])))
print(list(map(lambda x: abs(x), [1, 3, 5, 8, -3, -8, -9])))

# pow : 제곱값 반환
print(pow(2, 10))

# range
print(list(range(1, 11)))
print(list(range(0, -15, -1)))

# round, ceil, floor
import math

print(round(6.5781, 2))
print(round(6.58))
print(math.ceil(5.9))
print(math.floor(5.6))

# sorted: 정렬 후 반환
print(sorted([1, 3, 5, 8, -3, -8, -9]))

# sum
print(sum([1, 3, 5, 8, -3, -8, -9]))

# type: 자료형

print(type(3))
print(type({}))
print(type([]))

# zip 튜플로 반환
print(list(zip([1, 3, 5, 8, -3, -8, -9], [1, 3, 5, 8, -3, -8, -9])))



