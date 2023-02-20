# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def f(b,n):
    if n<b:
        return n
    else:
        return (f(b,math.floor(n/b))+ (n%b))

def find_i(n,s):
    t = 2
    #if there exists an integer b  such that f(b,n) = s. If such an integer b exists, find the smallest such b.
    while t < n:
        if f(t,n) == s:
            return t 
        t +=1
    return -1

n = int(input())
s = int(input())
print(find_i(n,s))