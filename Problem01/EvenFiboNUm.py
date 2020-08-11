def fib(max):
    x = 1
    y = 2
    while (x < max):
        yield x
        x, y = y, x + y

if __name__ == "__main__":
    print(sum(i for i in fib(10000000) if i % 2 == 0))
