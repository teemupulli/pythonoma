import random
print('%03d' % random.randint(0, 4**4-1))
a = ""

for i in range(4):
    a += str(random.randint(1,6))

print(a)