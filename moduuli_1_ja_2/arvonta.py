import random
print('%03d' % random.randint(0, 4**4-1))
print(random.randint(1111, 6666))

for i in range(4):

    i += random.randint(1,6)
print(i)