
import scipy.io
from matplotlib import pyplot as plt
import csv
import numpy as np
import copy




def find_goal(map,length,width):
    for i in range(length):
        for j in range(width):
            if map[i][j] == 2:
                return i,j


def the_filling(X_goal,Y_goal,map,length,width):
    NewXarray=([X_goal])
    NewYarray=([Y_goal])
    NewXarray, NewYarray =fill_the_matrix(NewXarray,NewYarray,map,length,width)
#     print("the newNewXarray XX ",NewXarray)
#     print("the NewYarray YY ",NewYarray)
#     print("thelenghth of x",len(NewXarray),"thelenghth of y",len(NewYarray))
    while(NewXarray or NewYarray ):
        NewXarray, NewYarray =fill_the_matrix(NewXarray,NewYarray,map,length,width)
      #   print("the newNewXarray XX ",NewXarray)
      #   print("the NewYarray YY ",NewYarray)
      #   print("thelenghth of x",len(NewXarray),"thelenghth of y",len(NewYarray))
#     return map
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
            # print("there is pixeles filed with",theNewValue)
            # print(' 1TH IF now the new YY array contian',NewYarray)
      if(currentXIndex<length and currentYIndex+1<width and map[currentXIndex,currentYIndex+1]==0):
            map[currentXIndex,currentYIndex+1]=theNewValue
            NewXarray.append(currentXIndex)
            NewYarray.append(currentYIndex+1)
            # print("there is pixeles filed with",theNewValue)
            # print('2TH IF now the new YY array contian',map[currentXIndex,currentYIndex+1])
      if(currentXIndex+1<length and currentYIndex+1<width and map[currentXIndex+1,currentYIndex+1]==0):
            map[currentXIndex+1,currentYIndex+1]=theNewValue
            NewXarray.append(currentXIndex+1)
            NewYarray.append(currentYIndex+1 )
            # print("there is pixeles filed with",theNewValue)
            # print('3TH IF now the new YY array contian',NewYarray)
      if(currentXIndex-1<length and currentYIndex-1<width and map[currentXIndex-1,currentYIndex-1]==0):
            map[currentXIndex-1,currentYIndex-1]=theNewValue
            NewXarray.append(currentXIndex-1)
            NewYarray.append(currentYIndex-1)
            # print("there is pixeles filed with",theNewValue)
            # print('4TH IF now the new YY array contian',NewYarray)
      if(currentXIndex-1<length and currentYIndex<width and map[currentXIndex-1,currentYIndex]==0):
            map[currentXIndex-1,currentYIndex]=theNewValue
            NewXarray.append(currentXIndex-1)
            NewYarray.append(currentYIndex)
            # print("there is pixeles filed with",theNewValue)
            # print('5TH IF now the new YY array contian',NewYarray)
      if(currentXIndex<length and currentYIndex-1<width and map[currentXIndex,currentYIndex-1]==0):
            map[currentXIndex,currentYIndex-1]=theNewValue
            NewXarray.append(currentXIndex)
            NewYarray.append(currentYIndex-1)
            # print("there is pixeles filed with",theNewValue)
            # print('6TH IF now the new YY array contian',NewYarray)
      if(currentXIndex-1<length and currentYIndex+1<width and map[currentXIndex-1,currentYIndex+1]==0):
            map[currentXIndex-1,currentYIndex+1]=theNewValue
            NewXarray.append(currentXIndex-1)
            NewYarray.append(currentYIndex+1)
            # print("there is pixeles filed with",theNewValue)
            # print('7TH IF now the new YY array contian',NewYarray)
      if(currentXIndex+1<length and currentYIndex-1<width and map[currentXIndex+1,currentYIndex-1]==0):
            map[currentXIndex+1,currentYIndex-1]=theNewValue
            NewXarray.append(currentXIndex+1)
            NewYarray.append(currentYIndex-1)
            # print("there is pixeles filed with",theNewValue)
            # print('8TH IF now the new YY array contian',NewYarray)
    return  NewXarray,NewYarray   
          
def trace_back(filled_mat,x_start,y_start,x_goal,y_goal,arr_of_coordinates):
      # x,y are the starting coordinates

      if filled_mat[x_start,y_start] == 2 or arr_of_coordinates[-1] == (x_goal,y_goal) :
            return arr_of_coordinates

      # check up
      up = [x_start,y_start-1]
      right = [x_start+1,y_start]
      down = [x_start,y_start+1]
      left = [x_start-1,y_start]
      upper_right = [x_start+1,y_start-1]
      lower_right = [x_start+1,y_start+1]
      lower_left = [x_start-1,y_start+1]
      upper_left = [x_start-1,y_start-1]


      if filled_mat[up[0],up[1]] < filled_mat[x_start,y_start]and filled_mat[up[0],up[1]] != 1:
            arr_of_coordinates.append((up[0],up[1]))
            trace_back(filled_mat,up[0],up[1],x_goal,y_goal,arr_of_coordinates)

      elif filled_mat[right[0],right[1]] < filled_mat[x_start,y_start]and filled_mat[right[0],right[1]] != 1:
            arr_of_coordinates.append((right[0],right[1]))
            trace_back(filled_mat,right[0],right[1],x_goal,y_goal,arr_of_coordinates)

      elif filled_mat[down[0],down[1]] < filled_mat[x_start,y_start]and filled_mat[down[0],down[1]] != 1:
            arr_of_coordinates.append((down[0],down[1]))
            trace_back(filled_mat,down[0],down[1],x_goal,y_goal,arr_of_coordinates)   

      elif filled_mat[left[0],left[1]] < filled_mat[x_start,y_start]and filled_mat[left[0],left[1]] != 1:
            arr_of_coordinates.append((left[0],left[1]))
            trace_back(filled_mat,left[0],left[1],x_goal,y_goal,arr_of_coordinates)


      elif filled_mat[upper_right[0],upper_right[1]] < filled_mat[x_start,y_start]and filled_mat[upper_right[0],upper_right[1]] != 1:
            arr_of_coordinates.append((upper_right[0],upper_right[1]))
            trace_back(filled_mat,upper_right[0],upper_right[1],x_goal,y_goal,arr_of_coordinates)
      
      elif filled_mat[lower_right[0],lower_right[1]] < filled_mat[x_start,y_start]and filled_mat[lower_right[0],lower_right[1]] != 1:
            arr_of_coordinates.append((lower_right[0],lower_right[1]))
            trace_back(filled_mat,lower_right[0],lower_right[1],x_goal,y_goal,arr_of_coordinates)
      
      elif filled_mat[lower_left[0],lower_left[1]] < filled_mat[x_start,y_start]and filled_mat[lower_left[0],lower_left[1]] != 1:
            arr_of_coordinates.append((lower_left[0],lower_left[1]))
            trace_back(filled_mat,lower_left[0],lower_left[1],x_goal,y_goal,arr_of_coordinates)

      elif filled_mat[upper_left[0],upper_left[1]] < filled_mat[x_start,y_start]and filled_mat[upper_left[0],upper_left[1]] != 1:
            arr_of_coordinates.append((upper_left[0],upper_left[1]))
            trace_back(filled_mat,upper_left[0],upper_left[1],x_goal,y_goal,arr_of_coordinates)
      print('no sol')
      return arr_of_coordinates

def planner(map,start_row,start_col):
      if map[start_col,start_row] == 1:
         print('forbidden place the program will start at 4,4')
         start_col = 4
         start_row = 4
      length=map.shape[0]
      width=map.shape[1]
      x_goal,y_goal=find_goal(map,length,width)

      value_map = copy.deepcopy(map)

      # modifies filled_map var
      the_filling(x_goal,y_goal,value_map,length,width)

      trajectory = trace_back(value_map,start_col,start_row,x_goal,y_goal,[(x_start,y_start)])

      return value_map,trajectory



# read input map
mat_file = scipy.io.loadmat('.\maze.mat') # returns a dict
map = mat_file['map']

map=np.asarray(map)
map=map.astype('uint32')

# plot original map(maze)
plt.imshow(map)
plt.show()

# get input from user
print("###############################################################################################")
print("'''''''FOR STARTING POINT''''''''")
print("Enter a number for rows between 0 and ",map.shape[0])
y_start = int(input())

print("Enter a number for columns between 0 and ",map.shape[1])
x_start = int(input())
print(type(x_start))
print(map[x_start,y_start])


value_map , trajectory = planner(map,x_start,y_start)



# plot value map
plt.imshow(value_map,cmap='gray')
plt.show()

print(trajectory)


# plot the maze with the solution path 
for coor_tuple in trajectory:
      map[coor_tuple] = 4
plt.imshow(map,cmap='gray')
plt.show()

