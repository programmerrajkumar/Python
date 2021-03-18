if 1 == 1:
    pass
elif 2 == 2:
    pass
else:
    pass

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:  # executes only if for loop is terminated by condition. not on break statement
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for i, v in enumerate(['tic', 'tac', 'toe']):  # use enumerate func to get index and item at same time
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

for i in range(3):
 print(i)