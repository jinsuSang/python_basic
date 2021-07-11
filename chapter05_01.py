# 함수

def print_hello(w):
    print('Hello', w)


word = 'Sunday'

print_hello(word)


def return_func(w):
    value = 'Hello ' + str(w)
    return value


x = return_func('Sunday')
print(x)


# 다중 반환

def mul(x):
    y1 = x * 10
    y2 = x * 100
    y3 = x * 1000
    return y1, y2, y3


print(mul(15))


# 중요 *args **kwargs

def args_func(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)


args_func('a', 'b', 'c')


def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('Result : {}'.format(v), kwargs.get(v))


kwargs_func(name1='kim', name2='sang')


def example(a1, a2, *args, **kwargs):
    print(a1, a2, args, kwargs)


example(10, 20, 'kim', 'sang', name1='jinsu', name2='wang')


# lambda
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 메모리 할당
# 람다는 즉시 실행 함수 힙 초기화 -> 메모리 초기화
# 많이 사용시 가독성 감소

# 일반 함수 변수 할당
def mul_func(x, y):
    return x * y


# 람다 함수 -> 할당
mul_lambda = lambda x, y: x * y

print(mul_func(5, 6))
print(mul_lambda(5, 6))


def func_final(a, b, func):
    print(a * b * func(a, b))


func_final(5, 6, lambda x, y: x * y)
