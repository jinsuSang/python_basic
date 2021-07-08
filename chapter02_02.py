n = 700

print(n)

# golang 에서는 reflect.TypeOf()
print(type(n))
print()

var = 75
var = 'Change string value'
print(var)
print(type(var))


n = 70
m = n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# id identity 확인 : 객체의 고유값 확인
m = 753
n = 159

print(id(m), id(n))
print(id(m) == id(n))
print()

m = 800
n = 800

print(id(m), id(n))
print(id(m) == id(n))
print()