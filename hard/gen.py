import csv
import pandas as pd
from random import random, randint

SZ = 88
NUMS = 4

with open('hard.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([''] * NUMS)
    fib = [0, 1]
    for i in range(2, SZ):
        fib.append(fib[-1] + fib[-2])
    for _ in range(250):
        if random() < 0.15:
            start = randint(0, SZ - NUMS)
            writer.writerow(fib[start:start + NUMS])
        else:
            writer.writerow([randint(1, 10**8) for i in range(4)])

pd.read_csv('hard.csv').to_excel('hard.xlsx', index=None, header=False)

f = open("hard.csv", 'r')
data = [list(map(int, i.split(','))) for i in f.readlines()[1:]]
f.close()
f = open("hard.csv", 'w', newline='')
writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for i in data:
    writer.writerow(i)
