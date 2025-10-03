t = (1, 2, 3, 4, 2, 7, 8, 8, 3, 2)
print(t)

repeated = []
print("Repeated elements in given tuple:")

for i in range(0, len(t)):
    if t.count(t[i]) > 1:
        if t[i] not in repeated:
            repeated.append(t[i])
            print(t[i])