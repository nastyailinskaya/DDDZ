array = [int(i) for i in input("Введите array: ").split()]
delta = int(input("Введите delta: "))
mmin = array[0]
for i in array:
    mmin = min(i, mmin)
cnt = 0
for i in array:
    if mmin + delta == i:
        cnt += 1
cnt += 1
print(cnt)
