def IsPower(x):
    while x % 2 == 0:
        x //= 2
    return x == 1


with open('medium.csv', 'r') as csvfile:
    ans = 0
    data = [list(map(int, s.split(','))) for s in csvfile.readlines()]
    for a in data:
        sm = sum(a)
        is_good = False
        for i in a:
            if IsPower(sm - i):
                is_good = True
        if is_good:
            ans += 1
    print(ans, file=open('ans.txt', 'w'))
