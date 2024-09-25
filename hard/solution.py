SZ = 88
with open('hard.csv', 'r') as csvfile:
    ans = 0
    data = [list(map(int, s.split(','))) for s in csvfile.readlines()]
    fib = [0, 1]
    for i in range(2, SZ):
        fib.append(fib[-1] + fib[-2])
    for a in data:
        k = 0
        while k < len(fib) and fib[k] < a[0]:
            k += 1
        is_good = True
        for i in range(4):
            if k + i >= len(fib) or fib[k + i] != a[i]:
                is_good = False
        if is_good:
            ans += 1
    print(ans, file=open('ans.txt', 'w'))
