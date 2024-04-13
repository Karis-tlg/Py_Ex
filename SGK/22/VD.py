A = [5, 2, 8, 3, 9, 1]

max = A[0]
a = 0
for i in range(len(A)):
    if A[i] > max:
        max = A[i]
        a = i
print(f"Max là: {max}, vị trí thứ: {a}")

min = A[0]
b = 0
for i in range(len(A)):
    if A[i] < min:
        min = A[i]
        b = i
print(f"Min là: {min}, vị trí thứ: {b}")
