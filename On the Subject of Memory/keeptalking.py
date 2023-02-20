def find_pos(i,n,array):
    for j in range (4):
        if array[i][j]==n:
            return j
in_array=input().strip()
array=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
array[0][0]=int(in_array[2])
array[0][1]=int(in_array[4])
array[0][2]=int(in_array[6])
array[0][3]=int(in_array[8])
array[0][4]=int(in_array[10])
array[1][0]=int(in_array[14])
array[1][1]=int(in_array[16])
array[1][2]=int(in_array[18])
array[1][3]=int(in_array[20])
array[1][4]=int(in_array[22])
array[2][0]=int(in_array[26])
array[2][1]=int(in_array[28])
array[2][2]=int(in_array[30])
array[2][3]=int(in_array[32])
array[2][4]=int(in_array[34])
array[3][0]=int(in_array[38])
array[3][1]=int(in_array[40])
array[3][2]=int(in_array[42])
array[3][3]=int(in_array[44])
array[3][4]=int(in_array[46])
array[4][0]=int(in_array[50])
array[4][1]=int(in_array[52])
array[4][2]=int(in_array[54])
array[4][3]=int(in_array[56])
array[4][4]=int(in_array[58])

position=[]
label=[]
code=""
#stage1
if array[0][4]==1:
    code+=str(array[0][1])
    position.append(1)
    label.append(array[0][1])
elif array[0][4]==2:
    code+=str(array[0][1])
    position.appaned(1)
    label.append(array[0][1])
elif array[0][4]==3:
    code+=str(array[0][2])
    position.append(2)
    label.append(array[0][2])
elif array[0][4]==4:
    code+=str(array[0][3])
    position.append(3)
    label.append(array[0][3])

#stage2
if array[1][4]==1:
    code+=4
    position.append(find_pos(1,4,array))
    label.append(4)
elif array[1][4]==2:
    code+=str(array[1][position[0]])
    position.append(position[0])
    label.append(array[1][position[0]])
elif array[1][4]==3:
    code+=str(array[1][0])
    position.append(0)
    label.append(array[1][0])
elif array[1][4]==4:
    code+=str(array[0][position[0]])
    position.append(position[0])
    label.append(array[1][position[0]])

#stage3
if array[2][4]==1:
    code+=str(label[1])
    position.append(find_pos(2,label[1],array))
    label.append(label[1])
elif array[2][4]==2:
    code+=str(label[0])
    position.append(find_pos(2,label[0],array))
    label.append(label[0])
elif array[2][4]==3:
    code+=str(array[2][2])
    position.append(2)
    label.append(array[2][2])
elif array[2][4]==4:
    code+=str(4)
    position.append(find_pos(2,4,array))
    label.append(4)

#stage4
if array[3][4]==1:
    code+=str(array[3][position[0]])
    position.append(position[0])
    label.append(array[3][position[0]])
elif array[3][4]==2:
    code+=str(array[3][0])
    position.appaned(0)
    label.append(array[3][0])
elif array[3][4]==3:
    code+=str(array[3][position[1]])
    position.append(position[1])
    label.append(array[3][position[1]])
elif array[3][4]==4:
    code+=str(array[3][position[1]])
    position.append(position[1])
    label.append(array[3][position[1]])

#stage5
if array[4][4]==1:
    code+=str(array[4][position[0]])
    position.append(position[0])
    label.append(array[4][position[0]])
elif array[4][4]==2:
    code+=str(array[4][position[1]])
    position.appaned(position[1])
    label.append(array[4][position[1]])
elif array[4][4]==3:
    code+=str(array[4][position[2]])
    position.append(position[2])
    label.append(array[4][position[2]])
elif array[4][4]==4:
    code+=str(array[4][position[3]])
    position.append(position[3])
    label.append(array[4][position[3]])
print(code)