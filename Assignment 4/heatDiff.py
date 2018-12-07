# Joshua Potter, jop13
# heatDiff.py

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
   temperature = float(input("Enter starting temperature: "))
   previousState = np.zeros([int(temperature)+2, int(temperature)+2])
   currentState = np.zeros([int(temperature)+2, int(temperature)+2])
   
   for i in range(0,int(temperature)+2):
      currentState[i,0] = temperature

   n = 0
   while n < 3000 and not np.array_equal(previousState, currentState):
      previousState = np.copy(currentState)
      for i in range(int(temperature)):       # columns
         i += 1
         for j in range(1,int(temperature)):     # rows
            currentState[i,j] = .25 * (previousState[i-1, j] + previousState[i+1, j] + previousState[i, j-1] + previousState[i, j+1])
            j += 1
      n += 1

   section = temperature // 8
   for i in range(1,int(temperature)):        # columns
      for j in range(1,int(temperature)):     # rows
         if currentState[i,j] <= section:
            plt.scatter(j,i,c="darkblue")
         elif section < currentState[i,j] < section*2:
            plt.scatter(j,i,c="blue")
         elif section*2 < currentState[i,j] < section*3:
            plt.scatter(j,i,c="aqua")
         elif section*3 < currentState[i,j] < section*4:
            plt.scatter(j,i,c="lawngreen")
         elif section*4 < currentState[i,j] < section*5:
            plt.scatter(j,i,c="yellow")
         elif section*5 < currentState[i,j] < section*6:
            plt.scatter(j,i,c="orange")
         elif section*6 < currentState[i,j] < section*7:
            plt.scatter(j,i,c="red")
         else:
            plt.scatter(j,i,c="darkred")

   plt.title("Heat Diffusion")
   plt.show()