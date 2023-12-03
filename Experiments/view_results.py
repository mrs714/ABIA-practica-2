import csv
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV data
data = []
with open("experiment-extensio2.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

# Separate data for True and False executions
true_data = [(int(row[1]), float(row[2])) for row in data[1:] if row[0] == 'True' ]
false_data = [(int(row[1]), float(row[2])) for row in data[1:] if row[0] == 'False' and float(row[2]) != 999 and int(row[1]) < 16] 

# Extract unique values for the x-axis (number of books)
x_values = sorted(set(true_data[i][0] for i in range(len(true_data))))
x = np.arange(len(x_values))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots()

offset = -width / 2
true_rects = ax.bar(x + offset, [np.mean([y for x_, y in true_data if x_ == val]) for val in x_values], width, label='True')
offset = width / 2
false_rects = ax.bar(x + offset, [np.mean([y for x_, y in false_data if x_ == val]) for val in x_values], width, label='False')

# Add labels, title and custom x-axis tick labels
ax.set_ylabel('Average Time')
ax.set_title('Average Time for Different Numbers of Books and Executions')
ax.set_xticks(x)
ax.set_xticklabels(x_values)
ax.legend(title="Sequential", bbox_to_anchor=(1, 1))

# Show the plot0
plt.show()
