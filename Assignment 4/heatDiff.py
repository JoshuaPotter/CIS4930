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

   #print(currentState)

   n = 0
   while n < 3000 and not np.array_equal(previousState, currentState):
      previousState = np.copy(currentState)
      for i in range(int(temperature)):       # columns
         i += 1
         for j in range(1,int(temperature)):     # rows
            currentState[i,j] = .25 * (previousState[i-1, j] + previousState[i+1, j] + previousState[i, j-1] + previousState[i, j+1])
            j += 1
      n += 1
   print(currentState)
   #axes.axis([0,int(temperature),0,int(temperature)])

   # section = temperature // 8
   # for i in range(1,int(temperature)):        # columns
   #    for j in range(1,int(temperature)):     # rows
   #       if currentState[i,j] < section:
   #          plt.scatter(j,i,c="darkblue")
   #       elif currentState[i,j]*2 <= section:
   #          plt.scatter(j,i,c="blue")
   #       elif currentState[i,j]*3 <= section:
   #          plt.scatter(j,i,c="aqua")
   #       elif currentState[i,j]*4 <= section:
   #          plt.scatter(j,i,c="lawngreen")
   #       elif currentState[i,j]*5 <= section:
   #          plt.scatter(j,i,c="yellow")
   #       elif currentState[i,j]*6 <= section:
   #          plt.scatter(j,i,c="orange")
   #       elif currentState[i,j]*7 <= section:
   #          plt.scatter(j,i,c="red")
   #       else:
   #          plt.scatter(j,i,c="darkred")

   plt.title("Heat Diffusion")
   plt.show()

   figure, axes = plt.subplots()
   data = axes.imshow(currentState, cmap=plt.get_cmap('hot'), interpolation='nearest', vmin=0, vmax=temperature)
   figure.colorbar(data)
   plt.show()
