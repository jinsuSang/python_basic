# for 반복문

for v1 in range(10):
    print(v1, end=' ')
print()

for v2 in range(1, 11, 3):
    print(v2, end=' ')
print()

for v3 in range(2, 11, 2):
    print(v3, end=' ')
print()

sum1 = 0
for v in range(1, 101):
    sum1 += v

print(sum1)
print(sum(range(1, 101)))

names = ['kim', 'sang', 'choi']

for name in names:
    print(name)

ex = ['1', 2, 3, True, 4.6, complex(5)]
for v in ex:
    if type(v) is str:
        continue
    print(v)

# for - else !!
# break 이 안되면 else 실행
nums = [14, 56, 89, 47, 22, 36, 14, 10, 25, 36, 38, 89, 100]

for num in nums:
    if num == 101:
        print('found')
        break
else:
    print('not found')
