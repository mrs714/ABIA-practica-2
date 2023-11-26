#!/bin/bash

# Amount of files generated by test_generator.py
files_init=1

# Number of iterations for each file
num_iterations=0

# Wether an iteration has run out of memory or not
out_of_memory=false

# Define lists
domain_files=()
for ((i=0; i<files_init; i++)); do
    domain_files+=("../FitxersPDDL/Domini_2.pddl")
done

problem_files=()
# problem_files+=("../JocsDeProva/testX_$i.pddl") for automatic generation, X level
# problem_files+=("../JocsDeProva/JocDeProvaXY.pddl") for manual generation, X level, Y problem (1 or 2)
for ((i=0; i<files_init; i++)); do
    problem_files+=("../JocsDeProva/JocDeProva21.pddl")
done

run_fluents=()
for ((i=0; i<files_init; i++)); do
    run_fluents+=(false)
done

planner="../FitxersPDDL/metricff.exe"



# Output file
output_file="experiment_results_.txt"

# Write the number of iterations and input files to the output file
echo "$num_iterations ${#domain_files[@]}" > $output_file

echo
echo "Starting experiments"
echo "Configuration:"
echo "Number of iterations: $num_iterations"
echo "Number of files: ${#domain_files[@]}"
echo "Planner: $planner"
echo "Output file: $output_file"
echo 

# Perform experiment for each element in the domain file list
for ((i=0; i<${#domain_files[@]}; i++)); do
    domain_file=${domain_files[i]}
    problem_file=${problem_files[i]}
    run_fluent=${run_fluents[i]}

    echo "------------------------------------------------------------------"
    echo
    echo "Running experiment for:"
    echo "Domain File: $domain_file"
    echo "Problem File: $problem_file"
    echo "Planner: $planner"
    echo "Command: $planner -o $domain_file -f $problem_file"

"$planner" -o "$domain_file" -f "$problem_file"

    # Run x iterations for each combination, plus one to see if the program runs out of memory
    if [ "$run_fluent" = false ]; then
        if "$planner" -o "$domain_file" -f "$problem_file" | grep -q "memory"; then
            echo "The program has run out of memory. Ending the loop."
            out_of_memory=true
            break
        else 
            echo "The program can be executed succesfully. Proceeding to timing:"
            echo
        fi
    else
        if "$planner" -o "$domain_file" -f "$problem_file" -O | grep -q "memory"; then
        echo "The program has run out of memory. Ending the loop."
        break
        else 
            echo "The program can be executed succesfully. Proceeding to timing:"
            echo
        fi
    fi

    for ((j=1; j<=$num_iterations; j++)); do
        echo "Iteration $j:"
	
        if [ "$run_fluent" = false ]; then
            { time "$planner" -o "$domain_file" -f "$problem_file"; } 2>&1 | grep real | tr ',' '.'| tee -a $output_file
        else
            { time "$planner" -o "$domain_file" -f "$problem_file" -O; } 2>&1 | grep real | tr ',' '.' | tee -a $output_file
        fi

        echo "Iteration $j completed"
        echo
    done

    echo "Experiment completed for $domain_file"
    echo
done
echo "------------------------------------------------------------------"
echo 

if [ "$out_of_memory" = true ]; then
    echo "An execution has run out of memory. Skipping the treatment of the data."
else
    echo "All experiments have been completed succesfully."
    echo
    echo "Proceeding to treat the data."
    echo
    # Execute the Python script to treat the data
    python3 process_results.py
    echo "Finished treating the data, files available at the execution directory"
    echo
fi
