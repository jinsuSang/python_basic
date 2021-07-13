# 외장 함수

import sys

print(sys.argv)

# 강제 종료
# sys.exit()

# 패키지 위치
print(sys.path)

# pickle 객체 파일 쓰기
import pickle

f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# os : 환경변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir rmdir rename
import os

print(os.environ)
print(os.environ.get('USERNAME'))
print(os.getcwd())

# time
import time

print(time.time())
print(time.localtime(time.time()))
print(time.ctime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

for i in range(5):
    print(i)
    time.sleep(.1)

# random
import random

print(random.random())
print(random.randint(1, 45))
print(random.randrange(1, 45))

d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

c = random.choice(d)
print(c)

# webbrowser

import webbrowser

webbrowser.open('https://github.com/jinsuSang')
webbrowser.open_new('https://github.com/jinsuSang')
