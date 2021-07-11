# 문자열

str1 = 'I am Python'
str2 = 'Python'
str3 = "What is your problem?"
str4 = '''Welcome!'''

print(len(str1))

# Raw String
raw_str1 = r'D:\python\test'
print(raw_str1)

# multi line
multi_str = \
'''
hi
hello
'''

print(multi_str)

# 연산

print('I' in str1)
print('P' not in str2)
print()

# 문자열 함수

strA = 'Python Golang Java'
print(strA.upper())
print(strA.capitalize())
print(strA.endswith('a'))
print(strA.replace('Java', 'Javascript'))
print(sorted(strA))
print(strA.split(' '))

print(dir(strA))
# __iter__

for i in strA:
    print(i)
print()

# slicing
print(strA[0])
print(strA[0:8])
print(strA[:7])
print(strA[5:])
print(strA[:len(strA)])
print(strA[:len(strA)-1])
print(strA[:])
print(strA[::2])
print(strA[::-1]) # 거꾸로 출력

a = 'A'
print(ord(a)) # 아스키 코드 65
print(chr(65)) # A
