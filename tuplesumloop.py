tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

result = tuple(tuple1[i] + tuple2[i] + tuple3[i] for i in range(len(tuple1)))

print("Element-wise sum:", result)
