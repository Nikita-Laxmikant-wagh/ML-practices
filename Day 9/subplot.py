import matplotlib.pyplot as plt

days=["Mon","Tue","Wed","Thu","Fri"]

temperature = [[22,24,21,27,25],
    [30,32,28,31,29],
    [25,27,24,26,28],
    [33,35,31,34,32]
]

cities=["Delhi","Mumbai","Bangalore","Chennai","Kolkata"]

fig, axs = plt.subplots(2, 2)

city_no = 0
for i in range(2):
    for j in range(2):
        axs[i, j].plot(days, temperature[city_no])
        axs[i, j].set_title(cities[city_no])
        city_no += 1
        

fig.suptitle("Temperature variation in different cities")
plt.tight_layout()
plt.show()




