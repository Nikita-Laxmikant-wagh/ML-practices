import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot with markers, dashed with dots lines, and blue color
plt.plot(x, y, marker='o', linestyle='-.', color='b')

# Create another line plot with markers, dashed lines, and blue color
plt.plot(x, y, marker='*', linestyle='--', color='b')

#` Create another line plot with markers, dotted lines, and blue color`
plt.plot(x, y, marker='*', linestyle=':', color='b')

plt.title('Sample Line Plot')

# assign labels to x and y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()  