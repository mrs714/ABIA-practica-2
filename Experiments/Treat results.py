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

        for line in file:
            parts = line.split('\t') # Format: real 0m0.000s 
            time = parts[1] # Format: 0m0.000s
            minutes = int(time.split('m')[0]) # Format: 0
            seconds = float(time.split('m')[1][:-2]) # Format: 0.000

            print(minutes, seconds)

        """
        num_iterations = int(first_line.split()[-1])

        # Initialize lists to store results for each experiment
        results_per_experiment = [[] for _ in range(num_iterations)]

        # Read subsequent lines and extract the relevant information
        for line in file:
            parts = line.split('\t')
            if len(parts) == 2 and parts[0] == 'real':
                # Extract the second part and remove 's'
                time_str = parts[1].strip('s')
                
                # Save the time in the corresponding list for the current experiment
                results_per_experiment[int((file.tell() - len(line)) / len(line)) % num_iterations].append(time_str)
                """

    return num_iterations, num_experiments

print(read_experiment_results(output_file))
# Example usage
"""
num_iterations, results_per_experiment = read_experiment_results(output_file)

# Print the results
print("Number of iterations per experiment:", num_iterations)
for i, experiment_results in enumerate(results_per_experiment):
    print(f"Experiment {i + 1} results:", experiment_results)
"""