import fileinput

for line in fileinput.input():
    input=line
input=input.split()
if(int(input[0])>15 or int(input[1])>15):
    print("No")
if(int(input[0])<int(input[1])):
    if(int(input[1])==int(input[0])*2 or int(input[1])==int(input[0])*2+1):
        print("Yes")
    else:
        print("No")
else:
    print("No")