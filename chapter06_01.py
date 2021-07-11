class Dog:
    species = 'dog'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return '{} is {} years old'.format(self.__name, self.__age)

    def shout(self, sound):
        print('{} shouts {}'.format(self.__name, sound))


print(Dog)

a = Dog('choco', 2)
b = Dog('white', 1)

print(a, a.__dict__)
print(b, b.__dict__)
print(Dog.species)


# self


class SelfTest:

    @classmethod
    def func1(cls):
        print('func1')

    def func2(self):
        print('func2')


SelfTest.func1()

f = SelfTest()
SelfTest.func2(f)


# 클래스 변수, 인스턴스 변수
class Warehouse:
    __stock_num = 0

    def __init__(self, name):
        self.__name = name
        Warehouse.__stock_num += 1

    def __del__(self):
        Warehouse.__stock_num -= 1

    @classmethod
    def stack_num(cls):
        return cls.__stock_num


wh1 = Warehouse('Yang')
wh2 = Warehouse('Shang')

print(wh1.stack_num())
print(wh2.stack_num())
print(Warehouse.stack_num())

del wh1
del wh2

print(Warehouse.stack_num())

# 상속

c = Dog('Coco', 3)
print(c)

d = Dog('Dodo', 5)
print(d)
d.shout('왈왈')
