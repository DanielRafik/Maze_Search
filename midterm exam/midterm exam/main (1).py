
import scipy.io
from matplotlib import pyplot as plt
import csv
import numpy as np
import copy

# increase the recursion limit
import sys
sys.setrecursionlimit(3000)



def find_goal(map,width):
    the_flateen=np.asarray(map)
    the_flateen=the_flateen.flatten()
    for m in range(len(the_flateen)):
        if the_flateen[m] == 2:
            theFirstIndixVal=m//width
            theSecondIndixVal=m-(width*theFirstIndixVal)
            print("the First Indix Val",theFirstIndixVal,"the Second IndixVal",theSecondIndixVal)
            return theFirstIndixVal,theSecondIndixVal

def fill_one_point(i,j,map,length,width,theNewValue,newXandYarray):
    if(i<length and j<width and map[i,j]==0):
          map[i,j]=theNewValue
          newXandYarray.append((i,j))
def the_filling(X_goal,Y_goal,map,length,width):
    #initialize the NewXandYarray with the x index of the goal and the y index of the goal  
    newXandYarray=[(X_goal,Y_goal)]
    #call fill_the_matrix function with 1 array x index of the goal and the y index of the goal  
    #it return a new array contian the indexs of the new values 
    newXandYarray=fill_the_matrix(newXandYarray,map,length,width)
    while(newXandYarray):
        #recall the fill_the_matrix function untill NewXandYarray is empty
        #when the array is empty this means no pixels fillled with the new value
        #the matrix is all filled 
        newXandYarray =fill_the_matrix(newXandYarray,map,length,width)
def fill_the_matrix(oldXandYarray,map,length,width):
    #set new array to store the x index and the y index of the values that will be filled 
    newXandYarray=[]
    
    for i in range(len(oldXandYarray)):
      currentXIndex,currentYIndex=oldXandYarray[i]
      theNewValue=map[currentXIndex,currentYIndex]+1 
      fill_one_point(currentXIndex+1,currentYIndex,map,length,width,theNewValue,newXandYarray)
      fill_one_point(currentXIndex,currentYIndex+1,map,length,width,theNewValue,newXandYarray)
      
      fill_one_point(currentXIndex+1,currentYIndex+1,map,length,width,theNewValue,newXandYarray)
      fill_one_point(currentXIndex-1,currentYIndex-1,map,length,width,theNewValue,newXandYarray)
      
      fill_one_point(currentXIndex-1,currentYIndex,map,length,width,theNewValue,newXandYarray)
      fill_one_point(currentXIndex,currentYIndex-1,map,length,width,theNewValue,newXandYarray)
      
      fill_one_point(currentXIndex-1,currentYIndex+1,map,length,width,theNewValue,newXandYarray)
      fill_one_point(currentXIndex+1,currentYIndex-1,map,length,width,theNewValue,newXandYarray)
    return  newXandYarray   
          
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
    try:
          if start_col>=map.shape[0] or start_row>=map.shape[1]:
             print('forbidden place the program will start at 4,4')
             start_col = 45
             start_row = 4
          if map[start_col,start_row] == 1:
             print('forbidden place the program will start at 4,4')
             start_col = 45
             start_row = 4
          length=map.shape[0]
          width=map.shape[1]
          x_goal,y_goal=find_goal(map,width)
    
          value_map = copy.deepcopy(map)
    
          # modifies filled_map var
          the_filling(x_goal,y_goal,value_map,length,width)
    
          trajectory = trace_back(value_map,start_col,start_row,x_goal,y_goal,[(start_col,start_row)])
    
          return value_map,trajectory
    except:
         print("there is an error occurred in the planner function")
          



# read input map
mat_file = scipy.io.loadmat('.\maze.mat') # returns a dict
map = mat_file['map']

map=np.asarray(map)
map=map.astype('uint32')

# plot original map(maze)
plt.imshow(map,cmap='gray')
plt.show()

# get input from user
print("###############################################################################################")
print("'''''''FOR STARTING POINT''''''''")

print("Enter a number for rows between 0 and ",map.shape[0])
y_start = int(input())

print("Enter a number for columns between 0 and ",map.shape[1])
x_start = int(input())

value_map , trajectory = planner(map,x_start,y_start)
# plot value map
plt.imshow(value_map,cmap='hot')
plt.show()

print(trajectory)


# plot the maze with the solution path 
for coor_tuple in trajectory:
      #print("the cor value ",coor_tuple)
      map[coor_tuple] = 4
plt.imshow(map,cmap='gray')
plt.show()


