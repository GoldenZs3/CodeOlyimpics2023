with open('keylog.txt',"r") as f:
    possible_numbers=[]
    lines=[]
    for line in f:
        lines.append(line.strip())
        if line[0] not in possible_numbers:
            possible_numbers.append(line[0])
        if line[1] not in possible_numbers:
            possible_numbers.append(line[1])
        if line[2] not in possible_numbers:
            possible_numbers.append(line[2])
    print("Ammount of unique characthers: "+str(len(possible_numbers)))
before={}
for i in possible_numbers:
    before[i]=""
for line in lines:
    if line[0] not in before[line[1]]:
        before[line[1]]+=line[0]
    if line[0] not in before[line[2]]:
       before[line[2]]+=line[0]
    if line[1] not in before[line[2]]:
        before[line[2]]+=line[1]
passw=""
while len(passw)<len(possible_numbers):
    for i in possible_numbers:
        if i not in passw and (before[i]=="" or sorted(passw)==sorted(before[i])):
            passw+=i
print(passw)   
    
