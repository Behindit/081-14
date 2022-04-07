import random

a = 1
b = 6

print(random.randint(a, b))

print(random.random())

random.seed(5)
k = random.randint(10, 20)
random.seed(5)
m = random.randint(10, 20)

print(k, m)

random.seed()
k = random.randint(10, 20)
random.seed()
m = random.randint(10, 20)

print(k, m)
