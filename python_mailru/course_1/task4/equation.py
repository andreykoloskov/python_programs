import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b ** 2 - 4 * a * c
y1 = (-b + d ** 0.5) / (2 * a)
y2 = (-b - d ** 0.5) / (2 * a)

print(int(y1))
print(int(y2))