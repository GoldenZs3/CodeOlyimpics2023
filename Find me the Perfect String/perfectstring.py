# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ones,zeros=input().split()
ones=int(ones)
zeros=int(zeros)
mod=998244353
number=2 #all 1s next to eachother and all 0s next to eachother
to_add=(math.factorial(ones+zeros)/(math.factorial(zeros)*math.factorial(ones)))-zeros-ones
number+=to_add
    
print(int(number%mod))