import os
import random

from graph_generator import BookGraph

# Get the directory of the currently executing script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Configuration: a test will be generated for each value of the list, with the given level and number of books
level = [0, 1, 2, 3] # 0: basic (0, 1 predecesor), 1: extension 1 (N predecesors), 2: extension 2 (M paralel), 3: extension 3 (pages)
num_books = [10, 15, 20, 30]
domain = "books"
predecessor_chance = [0.5, 0.5, 0.5, 0.5] # Chance of a book having a predecesor - level 0
parallel_chance = [0.5, 0.5, 0.5, 0.5] # Chance of a book having a parallel - level 2
page_range = (100, 500) # Range of pages for each book - level 3
random_seed = 42 # Set the random seed to get the same results

random.seed(random_seed)

# Collection of books
for test in range(len(level)):
    # Get the path of the problem file
    problem_name = "test" + str(level[test]) + "_" + str(test) + ".pddl"
    output_file = os.path.join(script_dir, problem_name)

    test_level = level[test]
    test_num_books = num_books[test]

    # Generate the graph
    graph = BookGraph(num_books=test_num_books, random_seed=random_seed, chance_predecesor_books=predecessor_chance, chance_parallel_books=parallel_chance)
    graph.generate_graph(test_level)

    # Get the node relations
    sequential_pairs = graph.get_sequetial_edge_nodes()
    parallel_pairs = graph.get_parallel_edge_nodes()

    with open(output_file, 'w') as problem_file:
        # Domain definition
        problem_file.write(f"(define (problem {problem_name})\n    (:domain {domain})\n")

        # Objects definition
        problem_file.write("    (:objects\n        ")
        for book in range(test_num_books):
            problem_file.write(f"book{book} ")
        problem_file.write("- book\n")
        problem_file.write("    )\n")

        # Initial state definition
        problem_file.write("    (:init\n")
        for book in range(test_num_books):

            # Level 3: pages
            if test_level == 3:
                pages = random.randint(page_range[0], page_range[1])
                problem_file.write(f"        (= (pages book{book}) {pages})\n")

        # Relationships between books
        for predecessor, book in sequential_pairs:
            problem_file.write(f"        (predecessor book{predecessor} book{book})\n")

        for parallel, book in parallel_pairs:
            problem_file.write(f"        (parallel book{parallel} book{book})\n")
            
        problem_file.write("    )\n")

        # Metrics: level 3
        if test_level == 3:
            pass
            # problem_file.write("    (:metric minimize (total-pages))\n") ??? esborrar abans d'entregar siusplau

        # Goal state definition
        problem_file.write("    (:goal\n")
        problem_file.write("    )\n")
        problem_file.write(")\n")


