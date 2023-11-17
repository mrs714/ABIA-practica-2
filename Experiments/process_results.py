import os
import csv

# Get the directory of the currently executing script
script_dir = os.path.dirname(os.path.realpath(__file__))

input_file = script_dir + "/experiment_results.txt"
output_file_averages = script_dir + "/experiment_results_averages.csv"
output_file_all = script_dir + "/experiment_results_all.csv"

def read_experiment_results(filename):
    with open(filename, 'r') as file:
        # Read the first line containing the number of iterations
        first_line = file.readline().strip() # Format: x y, where x is the number of iterations and y is the number of experiments

        num_iterations = int(first_line.split()[0])
        num_experiments = int(first_line.split()[1])

        results = [[] for _ in range(num_experiments)]

        for experiment in range(num_experiments):
            for iteration in range(num_iterations):
                # Read line
                line = file.readline().strip()
                parts = line.split('\t') # Format: real 0m0.000s 
                time = parts[1] # Format: 0m0.000s
                minutes = int(time.split('m')[0]) # Format: 0
                seconds = float(time.split('m')[1][:-1]) # Format: 0.000

                total = minutes * 60 + seconds # Format: 0.000

                results[experiment].append(total)
    return num_iterations, num_experiments, results

def treat_data(num_iterations, results_per_experiment, results):
    # Calculate average for each experiment
    averages = []
    for experiment in range(results_per_experiment):
        total = 0
        for iteration in range(num_iterations):
            total += results[experiment][iteration]
        averages.append(round(total / num_iterations, 3))
    return averages

def save_data(num_iterations, results_per_experiment, results, averages):
    # Save data to file in a csv format using the library csv
    with open(output_file_averages, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment", "Average"])
        for experiment in range(results_per_experiment):
            writer.writerow([experiment + 1, averages[experiment]])

    # Save also all the values from results
    with open(output_file_all, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment", "Iteration", "Time"])
        for experiment in range(results_per_experiment):
            for iteration in range(num_iterations):
                writer.writerow([experiment + 1, iteration + 1, results[experiment][iteration]])


num_iterations, results_per_experiment, full_results = read_experiment_results(input_file)
averages = treat_data(num_iterations, results_per_experiment, full_results)
save_data(num_iterations, results_per_experiment, full_results, averages)