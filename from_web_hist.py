import matplotlib.pyplot as plt 
import numpy as np  
   
#a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
a = np.array([0,0,0,0,56,0,55,54,0,0,51,0,0,0,0]) 
plt.hist(a, bins = [0,20,40,60,80,100]) 
plt.title("histogram") 
plt.show()
