a = input()
b = input()
z = ''.join('0' if i == j else '1' for i, j in zip(a,b))
print(z)
