# Exception 예외 처리
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, keyError ....
# runtime exception
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다
# 4. 예외 무시

# ZeroDivisionError
# print(100/0)

# IndexError
# x = [70,80,90]
# x[3]

# AttributeError 모듈 클래스에 있는 잘못된 속성 사용 예외
import time

# print(time.time2())

# TypeError
# x = [1, 2]
# y = 1, 2,
# print(x + y)

# 예외 처리

# try:
#
# except:
# except
# else:
#
# finally:


name = ['kim', 'lee', 'park']

try:
    z = 'sang'
    x = name.index(z)
except ValueError as ve:
    print('Not found')
else:
    print('This is else')
finally:
    print('Finally')
print()

try:
    a = 'park'
    if a == 'kim':
        print('pass')
    else:
        raise ValueError
except ValueError as ve:
    print(ve)
else:
    print('OK')
