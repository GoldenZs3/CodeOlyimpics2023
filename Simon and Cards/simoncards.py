# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
n,avg=input().strip().split()
n=int(n)
avg=int(avg)
cards=input().strip().split()
possibility=0
for subset in itertools.chain.from_iterable(
        itertools.combinations(cards, r) for r in range(len(cards)+1)):
    sum=0
    for element in subset:
        sum+=int(element)
    if len(subset)!=0 and sum/len(subset)==avg:
        possibility+=1
print(possibility)