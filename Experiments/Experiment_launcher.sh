#!/bin/bash

# Define lists
domain_files=("../Domini 1.pddl" "../Domini 2.pddl")
problem_files=("../Problema 1.pddl" "../Problema 2.pddl")
planners="../Fitxers PDDL/metricff.exe"
run_fluents=(false false true)

# Number of iterations
num_iterations=5

# Output file
output_file="experiment_results.txt"

# Write the number of iterations to the output file
echo "$num_iterations ${#domain_files[@]}" > $output_file

# Perform experiment for each element in the domain file list
for ((i=0; i<${#domain_files[@]}; i++)); do
    domain_file=${domain_files[i]}
    problem_file=${problem_files[i]}
    planner=${planners[i]}
    run_fluent=${run_fluents[i]}

    echo "Running experiment for:"
    echo "Domain File: $domain_file"
    echo "Problem File: $problem_file"
    echo "Planner: $planner"

    # Run x iterations for each combination
    for ((j=1; j<=$num_iterations; j++)); do
        echo "Iteration $j:"
	
        if [ "$run_fluent" = false ]; then
            { time $planner -o $domain_file -f $problem_file; } 2>&1 | grep real | tee -a $output_file
        else
            { time $planner -o $domain_file -f $problem_file -O; } 2>&1 | grep real | tee -a $output_file
        fi

        echo "Iteration $j completed"
        echo
    done

    echo "Experiment completed for $domain_file"
    echo
done

# Execute the Python script to treat the data
python3 process_results.py

echo "Finished treating the data, files available at the execution directory"