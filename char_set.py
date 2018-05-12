sum = 0
for i in range(2, 101):
    if i % 2 == 0:
        i = i * 1
    else:
        i = i * (-1)
    sum = sum + i
print(sum)