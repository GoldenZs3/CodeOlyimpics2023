# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

for line in fileinput.input():
    id=line.strip()
number=0
index=len(id)-1
for letter in id:
    number+=(ord(letter)-64)*(26**index)
    index-=1
print(number)