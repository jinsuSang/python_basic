# CSV 파일
import csv

with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)

    # 헤더 생략
    next(reader)

    for c in reader:
        print(c)

with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('===============')

w = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

with open('./resource/write1.csv', 'w', encoding='UTF-8', newline='') as f:
    wt = csv.writer(f)

    for value in w:
        wt.writerow(value)

with open('./resource/write2.csv', 'w', encoding='UTF-8', newline='') as f:
    fields = ['first', 'second', 'third']
    wt = csv.DictWriter(f, fieldnames=fields)
    wt.writeheader()

    for v in w:
        d = dict(
            first=v[0],
            second=v[1],
            third=v[2]
        )

        wt.writerow(d)