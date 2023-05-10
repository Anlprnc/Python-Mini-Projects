x, y = 0, 1

print(x)
print(y)

n = 10
for i in range(2, n):
    z = x + y
    print(z)
    x = y
    y = z
