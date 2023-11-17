import os

# Get the directory of the currently executing script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Now 'script_dir' contains the full path to the directory
print("Current script directory:", script_dir)


output_file = script_dir + "./experiment_results.txt"

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
        averages.append(total / num_iterations)
    return averages


num_iterations, results_per_experiment, full_results = read_experiment_results(output_file)
averages = treat_data(num_iterations, results_per_experiment, full_results)

