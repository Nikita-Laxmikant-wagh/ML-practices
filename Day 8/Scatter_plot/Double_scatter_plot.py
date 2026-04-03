import matplotlib.pyplot as plt

cities = ["Nashik", "Mumbai", "Pune", "Dhule", "Aurangabad","Nandurbar"]

summer_temperature = [35, 32, 33, 38, 36, 40]
summer_humidity = [60, 70, 65, 55, 68, 50]

winter_temperature = [20, 18, 22, 15, 19, 12]   
winter_humidity = [80, 85, 78, 90, 82, 88]

plt.scatter(summer_temperature, summer_humidity, color='r', label='Summer', marker='o')
for i in range(len(cities)):
    plt.annotate(cities[i], xy=(summer_temperature[i], summer_humidity[i]), xytext=(summer_temperature[i]+0.5, summer_humidity[i]+0.5), ha='center')


plt.scatter(winter_temperature, winter_humidity, color='b', label='Winter', marker='s')
for i in range(len(cities)):
    plt.annotate(cities[i], xy=(winter_temperature[i], winter_humidity[i]), xytext=(winter_temperature[i]+0.5, winter_humidity[i]+0.5), ha='center')

plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Temperature vs Humidity in Different Cities')
plt.legend()
plt.grid(True)
plt.show()

