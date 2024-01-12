import csv
from collections import Counter

# subway.csv 파일을 읽어 승하차 인원이 많은 지하철역 TOP 5를 뽑아보자

def subway():
    in_counter = Counter()      # dictionary
    out_counter = Counter()

    with open('subway.csv', encoding='utf-8') as f:
        f.readline()
        f.readline()

        reader = csv.reader(f)

        for line in reader:
            # 승차인원, 하차인원 뽑기
            in_num = line[3].strip()
            out_num = line[4].strip()

            # key = 호선명 + 지하철역
            key = line[1].strip() + ' ' + line[2].strip()

            in_counter[key] += int(in_num)
            out_counter[key] += int(out_num)

        print('< 승차인원 TOP 5 >')
        for data in in_counter.most_common(5):
            print(data[0], data[1])

        print('< 하차인원 TOP 5 >')
        for data in out_counter.most_common(5):
            print(data[0], data[1])

subway()
