import matplotlib.pyplot as plt

Patients = ["Patient A", "Patient B", "Patient C", "Patient D", "Patient E"]    
Blood_Pressure = [120, 130, 110, 140, 125]
Heart_Rate = [80, 85, 75, 90, 82]

#  Draw a Scatter plot with Blood Pressure on x-axis and Heart Rate on y-axis
plt.scatter(Blood_Pressure, Heart_Rate, cmap='plasma',c=Blood_Pressure, label='Patients')

# plot a colorbar to show the range of Blood Pressure values
plt.colorbar(label='Blood Pressure')  

# Annotate each point with the corresponding patient name
for i in range(len(Patients)):
    plt.annotate(Patients[i], xy=(Blood_Pressure[i], Heart_Rate[i]), xytext=(Blood_Pressure[i], Heart_Rate[i]), ha='center')

plt.title('Blood Pressure vs Heart Rate of Patients')       
plt.xlabel('Blood Pressure')
plt.ylabel('Heart Rate')
plt.legend()
plt.grid()
plt.show()