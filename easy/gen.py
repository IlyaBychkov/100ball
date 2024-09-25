import csv
import pandas as pd
from random import randint

NUMS = 5

with open('easy.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([''] * NUMS)
    for _ in range(250):
        writer.writerow([randint(1, 150) for i in range(NUMS)])

pd.read_csv('easy.csv').to_excel('easy.xlsx', index=None, header=False)

f = open("easy.csv", 'r')
data = [list(map(int, i.split(','))) for i in f.readlines()[1:]]
f.close()
f = open("easy.csv", 'w', newline='')
writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for i in data:
    writer.writerow(i)
