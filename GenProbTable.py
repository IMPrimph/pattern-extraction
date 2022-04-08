import os

num_lines = sum(1 for line in open('./REPatterns.txt'))

obj = {}

for line in open('./REPatterns.txt'):
    if line in obj:
        obj[line] += 1
    else:
        obj[line] = 1

uniqueLinesCount = len(obj.keys())

res = {}

i = 1

for line in open('./REPatterns.txt'):
    res['P{}'.format(i)] = obj[line] / num_lines
    i += 1

print(res)
