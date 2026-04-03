import matplotlib.pyplot as plt

student_names = ["Atharv", "Bhavesh", "Charu", "Devika", "Esha", "karuna", "Graurav", "Harsha", "Aman", "Juli"]
student_marks =[78,69,80,70,88,91,72,85,90,82]


plt.bar(student_names, student_marks, color='b', label='Marks')

plt.title('Student Marks') 
plt.xlabel('Students')
plt.ylabel('Marks')

plt.grid()
plt.show()