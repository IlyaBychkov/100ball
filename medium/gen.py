import csv
import pandas as pd
from random import random, randint, shuffle

NUMS = 4

with open('medium.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([''] * NUMS)
    for _ in range(250):
        if random() < 0.15:
            number = 2 ** randint(2, 20)
            a = randint(1, number - 2)
            number -= a
            b = randint(1, number - 1)
            number -= b
            c = number
            li = [a, b, c, randint(1, 500000)]
            shuffle(li)
            writer.writerow(li)
        else:
            writer.writerow([randint(1, 500000) for i in range(4)])

pd.read_csv('medium.csv').to_excel('medium.xlsx', index=None, header=False)

f = open("medium.csv", 'r')
data = [list(map(int, i.split(','))) for i in f.readlines()[1:]]
f.close()
f = open("medium.csv", 'w', newline='')
writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for i in data:
    writer.writerow(i)



