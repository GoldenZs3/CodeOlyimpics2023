# Enter your code here. Read input from STDIN. Print output to STDOUT
def query(array):
    numbers={}
    pairs=0
    for i in array:
        try:
            numbers[i]+=1
        except:
            numbers[i]=1
    for key in numbers.keys():
        pairs+=int(numbers[key]/2)
    return int(pairs)
    
n=int(input())
colours = list(map(int, input().strip().split()))
q=int(input())
for _ in range(q):
    line=input().strip().split()
    print(query(colours[int(line[0])-1:int(line[1])]))