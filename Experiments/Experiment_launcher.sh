#!/bin/bash

# Define lists
domain_files=("../Domini 1.pddl")
problem_files=("../Problema 1.pddl")
planners="../Fitxers PDDL/metricff.exe"
run_fluents=(false false true)

# Number of iterations
num_iterations=5

# Perform experiment for each element in the domain file list
for ((i=0; i<${#domain_files[@]}; i++)); do
    domain_file=${domain_files[i]}
    problem_file=${problem_files[i]}
    planner=${planners[i]}

    echo "Running experiment for:"
    echo "Domain File: $domain_file"
    echo "Problem File: $problem_file"
    echo "Planner: $planner"

    # Run x iterations for each combination
    for ((j=1; j<=$num_iterations; j++)); do
        echo "Iteration $j:"
	
	if [ "$run_command" = false ]; then
        
        	{ time $planner -o $domain_file -f $problem_file; } 2>&1 | grep real

        	echo "Iteration $j completed"
        	echo
	else
		{ time $planner -o $domain_file -f $problem_file -O; } 2>&1 | grep real

        	echo "Iteration $j completed"
        	echo
    done

    echo "Experiment completed for $domain_file"
    echo
done
