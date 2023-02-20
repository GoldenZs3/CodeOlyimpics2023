# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
def count_assignments(K, S):
    count = 0
    for x in range(max(0, S - 2*K), min(S, K)+1):
        for y in range(max(0, S - 2*K - x), min(S-x, K)+1):
            z = S - x - y
            if z >= 0 and z <= K:
                count += 1
    return count
for line in fileinput.input():
    input=line
k,s=input.split()
k=int(k)
s=int(s)
if(s/3==k):
    print(1)
else:
    print(count_assignments(k,s))