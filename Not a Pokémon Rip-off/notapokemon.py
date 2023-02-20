# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y, a, b = map(int, input().split())

exp = 0

while x < y and (x * a) <= x + b:
    x *= a
    exp += 1

exp += (y - x - 1) // b

print(exp)