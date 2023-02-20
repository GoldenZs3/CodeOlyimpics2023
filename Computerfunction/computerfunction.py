def computerfunction(a,b):
    #the function is a bitwise XOR
    return a^b
inputs=input().split()
print(computerfunction(int(inputs[0]),int(inputs[1])))