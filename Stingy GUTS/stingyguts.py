# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b,c,x = map(int, input().strip().split())
if x<=a:
    possibility=1
elif x>b:
    possibility=0
else:
    possibility=c/(b-a)
print(f"{possibility:.12f}")