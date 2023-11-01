# ciclo for
print("Ciclo for")
for i in range(1, 11):
    print(i)


# ciclo while sin break
k = 1
print("Ciclo while sin break")
while k <= 10:
    print(k)
    k += 1

# ciclo while con break
j = 1
print("Ciclo while con break")
while j <= 10:
    print(j)
    if j == 5:
        break
    j += 1

# ciclo while con continue
i = 0
print("Ciclo while con continue")
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)