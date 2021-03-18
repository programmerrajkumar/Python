def CustomRange(start, end, step=1):
    while start <= end:
        yield start
        start += step


for x in CustomRange(1, 5, 2): print(x)
