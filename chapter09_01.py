# 파일 읽기 및 쓰기

# 읽기 모드: r, 쓰기모드 w, 추가모드 a, 텍스트 모드 t, 바이너리 모드 b

# 파일 읽기
f = open('./resource/it_news.txt', 'rt', encoding='UTF-8')

print(f.encoding, f.name, f.mode)

cts = f.read()
print(cts)

f.close()

# with, close 생략
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# read(10) 10 byte 만 읽음
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)

print()

# readline : 한 줄 읽기
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    line = f.readline()
    print(line)

print()

# readlines : 전체를 읽고 라인 단위로 리스트 반환
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()

# 파일 쓰기

with open('./resource/contents1.txt', 'w') as f:
    f.write('I maybe love python\n')

with open('./resource/contents1.txt', 'a') as f:
    f.write('I maybe love python 2\n')

# writelines 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    li = ['Fried Chicken\n', 'Coffee\n', 'Ramen\n']
    f.writelines(li)

# print 활용
with open('./resource/contents3.txt', 'w') as f:
    print('Text Write', file=f)
    print('Text Write', file=f)
    print('Text Write', file=f)