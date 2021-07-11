# dictionary
# 순서 없음, 키 중복 불가

a = {
    'name': 'jinsu',
    'phone': '01012345678',
    'birth': '950309'
}

aT = dict([
    ('name', 'jinsu'),
    ('phone', '01012345678'),
    ('birth', '950309')
])

f = dict(
    name='jinsu',
    city='seoul',
    age=27
)

print(f['name'], f.get('name'))
print(f['name'])  # 존재 X -> 에러발생
print(f.get('names'))  # 존재 1X -> None 처리

# 추가
f['address'] = 'incheon'
print(f)


# dict_keys, values, items __iter__
print(f.keys())
print(f.values())
print(f.items())

for key in list(f.keys()):
    print(f.get(key))

print(f.pop('name'))
print(f)

print(f.popitem())
print(f.popitem())

print()

print('name' in a)

f.update(birth='950309')
print(f)
