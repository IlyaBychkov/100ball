fib = [0, 1]
while fib[-1] + fib[-2] < 1e18:
    fib.append(fib[-1] + fib[-2])
print(len(fib))
