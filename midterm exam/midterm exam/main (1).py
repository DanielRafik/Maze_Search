
import scipy.io
from matplotlib import pyplot as plt
import csv
import numpy as np



def find_goal():
    for i in range(length):
        for j in range(width):
            if map[i][j] == 2:
                return i,j

def the_filling(X,Y,map,length,width):
    NewXarray=([X])
    NewYarray=([Y])
    NewXarray, NewYarray =fill_the_matrix(NewXarray,NewYarray,map,length,width)
    print("the newNewXarray XX ",NewXarray)
    print("the NewYarray YY ",NewYarray)
    print("thelenghth of x",len(NewXarray),"thelenghth of y",len(NewYarray))
    while(NewXarray or NewYarray ):
        NewXarray, NewYarray =fill_the_matrix(NewXarray,NewYarray,map,length,width)
        print("the newNewXarray XX ",NewXarray)
        print("the NewYarray YY ",NewYarray)
        print("thelenghth of x",len(NewXarray),"thelenghth of y",len(NewYarray))
def fill_the_matrix(arrayX,arrayY,map,length,width):
    NewXarray=[]
    NewYarray=[]
    for i in range(len(arrayX)):
      currentXIndex=arrayX[i]
      currentYIndex=arrayY[i]  
      theNewValue=map[currentXIndex,currentYIndex]+1 
      if(currentXIndex+1<length and currentYIndex<width and map[currentXIndex+1,currentYIndex]==0):
            map[currentXIndex+1,currentYIndex]=theNewValue
            NewXarray.append(currentXIndex+1)
            NewYarray.append(currentYIndex )
            print("there is pixeles filed with",theNewValue)
            print(' 1TH IF now the new YY array contian',NewYarray)
      if(currentXIndex<length and currentYIndex+1<width and map[currentXIndex,currentYIndex+1]==0):
            map[currentXIndex,currentYIndex+1]=theNewValue
            NewXarray.append(currentXIndex)
            NewYarray.append(currentYIndex+1)
            print("there is pixeles filed with",theNewValue)
            print('2TH IF now the new YY array contian',NewYarray)
      if(currentXIndex+1<length and currentYIndex+1<width and map[currentXIndex+1,currentYIndex+1]==0):
            map[currentXIndex+1,currentYIndex+1]=theNewValue
            NewXarray.append(currentXIndex+1)
            NewYarray.append(currentYIndex+1 )
            print("there is pixeles filed with",theNewValue)
            print('3TH IF now the new YY array contian',NewYarray)
      if(currentXIndex-1<length and currentYIndex-1<width and map[currentXIndex-1,currentYIndex-1]==0):
            map[currentXIndex-1,currentYIndex-1]=theNewValue
            NewXarray.append(currentXIndex-1)
            NewYarray.append(currentYIndex-1)
            print("there is pixeles filed with",theNewValue)
            print('4TH IF now the new YY array contian',NewYarray)
      if(currentXIndex-1<length and currentYIndex<width and map[currentXIndex-1,currentYIndex]==0):
            map[currentXIndex-1,currentYIndex]=theNewValue
            NewXarray.append(currentXIndex-1)
            NewYarray.append(currentYIndex)
            print("there is pixeles filed with",theNewValue)
            print('5TH IF now the new YY array contian',NewYarray)
      if(currentXIndex<length and currentYIndex-1<width and map[currentXIndex,currentYIndex-1]==0):
            map[currentXIndex,currentYIndex-1]=theNewValue
            NewXarray.append(currentXIndex)
            NewYarray.append(currentYIndex-1)
            print("there is pixeles filed with",theNewValue)
            print('6TH IF now the new YY array contian',NewYarray)
      if(currentXIndex-1<length and currentYIndex+1<width and map[currentXIndex-1,currentYIndex+1]==0):
            map[currentXIndex-1,currentYIndex+1]=theNewValue
            NewXarray.append(currentXIndex-1)
            NewYarray.append(currentYIndex+1)
            print("there is pixeles filed with",theNewValue)
            print('7TH IF now the new YY array contian',NewYarray)
      if(currentXIndex+1<length and currentYIndex-1<width and map[currentXIndex+1,currentYIndex-1]==0):
            map[currentXIndex+1,currentYIndex-1]=theNewValue
            NewXarray.append(currentXIndex+1)
            NewYarray.append(currentYIndex-1)
            print("there is pixeles filed with",theNewValue)
            print('8TH IF now the new YY array contian',NewYarray)
    return  NewXarray,NewYarray   
          

            



mat_file = scipy.io.loadmat('midterm exam\maze.mat') # returns a dict
map = mat_file['map']
# map = map[100:150,100:150]
length=map.shape[0]
width=map.shape[1]
print("the length ",length,"the width",width)
plt.imshow(map)
plt.show()
x=4
y=149
plt.imshow(map)
map=np.asarray(map)
map=map.astype('uint32')

plt.show()
the_filling(x,y,map,length,width)
with open('sample.csv', 'w') as f:
    mywriter = csv.writer(f, delimiter=',')
    mywriter.writerows(map)    

plt.imshow(map)
plt.show()

