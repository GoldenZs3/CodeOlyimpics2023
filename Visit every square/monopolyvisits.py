#Monopoly board consists of 40 squares
import random
visited=[False]*40
all_visited=False
circuits=0
rolls=0
position=0
visited[0]=True     #set it so that the start is visted (as we start there)
while not all_visited:
    rolls+=1
    #roll 2d6
    step1=random.randint(1,6)
    step2=random.randint(1,6)
    position=position+step1+step2
    if position>=40:
        position=position-40
        circuits+=1
    visited[position]=True
    print("Roll number: "+ str(rolls))
    print("Position: "+ str(position))
    print("Number of circuits finished: "+str(circuits))
    if False not in visited:
        all_visited=True
print("--------- All the squares have been visited --------")
print("Overall number of rolls: "+str(rolls))
print("Overall finished circuits: "+str(circuits))
