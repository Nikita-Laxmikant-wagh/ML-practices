import matplotlib.pyplot as plt

student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]

student_scores = [85, 92, 78, 90, 88]

student_study_hours = [2, 4, 1.5, 3, 2.5]

# Create a line plot for student scores with markers, dashed lines, and blue color
plt.plot(student_scores, student_study_hours, marker='o', linestyle='--', color='b', label='Scores')

plt.title('Student Scores and Study Hours')
plt.xlabel('Student Scores')
plt.ylabel('Study Hours')
plt.legend()        
plt.grid()
plt.show()


