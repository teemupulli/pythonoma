print("Anna leiviskät.")
a = int(input())
print("Anna naulat.")
b = int(input())
print("Anna luodit.")
c = int(input())

a = a *20 * 32 * 13.3
c = c *13.3
b = b * 32 * 13.3

print(a+b+c)

d = int(a + b + c)%1000

e = int((a+b+c)//1000)

print("Massa nykymittojen mukaan:")
print(str(e) + " kilogrammaa " + str(d) + " grammaa")