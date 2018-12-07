# Joshua Potter, jop13
# heatDiff.py

import numpy as np
import matplotlib.pyplot as plt

def colorPicker(temperature,currentState):
   integer = int(currentState)
   colors = ['darkred','red','orange','yellow','lawngreen','aqua','blue','darkblue']
   index = 0
   
   if currentState < temperature//8:
      index = 7
   elif currentState < temperature//7:
      index = 6
   elif currentState < temperature//6:
      index = 5
   elif currentState < temperature//5:
      index = 4
   elif currentState < temperature//4:
      index = 3
   elif currentState < temperature//3:
      index = 2
   elif currentState < temperature//2:
      index = 1
   else:
      index = 0

   return colors[index]

if __name__ == "__main__":
   temperature = float(input("Enter starting temperature: "))
   previousState = np.zeros([int(temperature)+2, int(temperature)+2])
   currentState = np.zeros([int(temperature)+2, int(temperature)+2])
   
   for i in range(0,int(temperature)+2):
      previousState[i,0] = temperature
      currentState[i,0] = temperature

   for i in range(1,int(temperature)+1):       # columns
      for j in range(1,int(temperature)+1):     # rows
         # print(previousState[i-1, j])
         # print(previousState[i+1, j])
         # print(previousState[i, j-1])
         # print(previousState[i, j+1])
         #print(round(.25 * (previousState[i-1, j] + previousState[i+1, j] + previousState[i, j-1] + previousState[i, j+1]), 2))
         currentState[i,j] = round(.25 * (previousState[i-1, j] + previousState[i+1, j] + previousState[i, j-1] + previousState[i, j+1]), 2)
         previousState[i,j] = currentState[i,j]

   #print(currentState)

   #axes.axis([0,int(temperature),0,int(temperature)])
   for i in range(1,int(temperature)+1):        # columns
      for j in range(1,int(temperature)+1):     # rows
         plt.scatter(i,j,marker='o',color=colorPicker(temperature,currentState[i,j]))

   plt.title("Heat Diffusion")
   plt.show()
