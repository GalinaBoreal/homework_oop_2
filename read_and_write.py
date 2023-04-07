
from pprint import pprint

read_files = {}
count_sort = []

count_file_1 = 0
with open('1.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        count_file_1 += 1
    count_sort.append(count_file_1)

with open('1.txt', encoding='utf-8') as f:
    result = f.readlines()
read_files.setdefault('1.txt', {count_file_1: result})

count_file_2 = 0
with open('2.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        count_file_2 += 1
    count_sort.append(count_file_2)

with open('2.txt', 'rt', encoding='utf-8') as f:
    result = f.readlines()
read_files.setdefault('2.txt', {count_file_2: result})

count_file_3 = 0
with open('3.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        count_file_3 += 1
    count_sort.append(count_file_3)

with open('3.txt', 'rt', encoding='utf-8') as f:
    result = f.readlines()
read_files.setdefault('3.txt', {count_file_3: result})

# pprint(read_files)

with open('4.txt', 'at', encoding='utf-8') as f:
    for num in sorted(count_sort):
        for key, val in read_files.items():
            for k, v in val.items():
                if num == k:
                    f.write((str(key)) + '\n')
                    f.write((str(k)) + '\n')
                    f.write(str(''.join(v)))
