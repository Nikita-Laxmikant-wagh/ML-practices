import matplotlib.pyplot as plt
import numpy as np

veg_persons = ["priya", "nikita", "aarya", "rohan", "aaysha"]
non_veg_persons = ["aashish", "Gauri", "Harshad", "Isha", "Juli"]

day =[1,2,3,4,5]

ratings_veg = [4.5, 4.0, 4.2, 3.8, 4.7]
ratings_non_veg = [3.5, 4.2, 4.0 , 4.5, 3.8]

x= np.arange(len(day))
width =0.4

plt.bar(x-width/2, ratings_veg,width, color='g', label='Veg')
plt.bar(x+width/2, ratings_non_veg, width,color='r', label='Non-Veg')

plt.title('Ratings of Veg and Non-Veg Dishes Over the day') 
plt.xlabel('Days')
plt.ylabel('Ratings')

plt.grid()
plt.legend()
plt.show()