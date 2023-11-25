import os
import random

from graph_generator import BookGraph

# Get the directory of the currently executing script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Wether to show the book graph when creating each test
show_graph = True

# Configuration: a test will be generated for each value of the list, with the given level and number of books
#level = [0, 1, 2, 3] # 0: basic (0, 1 predecesor), 1: extension 1 (N predecesors), 2: extension 2 (M paralel), 3: extension 3 (pages)
#num_books = [30, 15, 20, 50]

config_range = 1

level = [1 for i in range(config_range)]
num_books = [5 + i for i in range(config_range)]
domain = "books"
predecessor_chance = [0.5 for i in range(config_range)] # Chance of a book having a predecesor - level 0
parallel_chance = [0.1 for i in range(config_range)] # Chance of a book having a parallel - level 2
read_books_percentage = [0.3 for i in range(config_range)] # Percentage of books that have been read
books_to_read_percentage = [0.3 for i in range(config_range)] # Percentage of books that the user wants to read
random_seed = 42 # Set the random seed to get the same results

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]

random.seed(random_seed)

# Collection of books
for test in range(len(level)):
    # Get the path of the problem file
    problem_name = "test" + str(level[test]) + "_" + str(test)
    problem_name_path = problem_name + ".pddl"
    output_file = os.path.join(script_dir, problem_name_path)

    test_level = level[test]
    test_num_books = num_books[test]
    test_predecessor_chance = predecessor_chance[test]
    test_parallel_chance = parallel_chance[test]

    max_pages = min(8000//test_num_books, 800)
    min_pages = max_pages//2

    # Generate the graph
    graph = BookGraph(num_books=test_num_books, random_seed=random_seed, chance_predecesor_books=test_predecessor_chance, chance_parallel_books=test_parallel_chance)
    graph.generate_graph(test_level)

    # Get the node relations
    sequential_pairs = graph.get_sequetial_edge_nodes()
    parallel_pairs = graph.get_parallel_edge_nodes()

    # Get the books that have been read, and the books that the user wants to read
    available_books = list(range(test_num_books))
    read_books = set(random.sample(available_books, int(test_num_books*read_books_percentage[test])))
    available_books = list(set(available_books) - read_books)
    books_to_read = set(random.sample(available_books, int(test_num_books*books_to_read_percentage[test])))
    available_books = list(set(available_books) - books_to_read)

    """
    def make_book_read_recursively(book):
        read_books.add(book)
        # Get the predecessors of the book
        predecessors = [book[0] for book in sequential_pairs if book[1] == book]
        # Mark the predecessors as read
        for successor in predecessors:
            make_book_read_recursively(successor)

    # If any book to be read has a parallel edge to a book that has already been read, mark all its predecessors as read
    parallel_books = [book[0] for book in parallel_pairs if book[1] in books_to_read]
    for book_with_parallel in parallel_books:
        predecessors = [book[0] for book in sequential_pairs if book[1] == book_with_parallel]
        for predecessor in predecessors:
            make_book_read_recursively(book_with_parallel)
    
    # Remove the books that have been read from the books to read
    books_to_read = books_to_read - read_books
    """

    print(f"Test {test}: {test_num_books} books, {len(sequential_pairs)} sequential pairs, {len(parallel_pairs)} parallel pairs, {len(read_books)} read books, {len(books_to_read)} books to read")
    if show_graph:
        graph.paint_reading_plan(read_books, books_to_read)

    with open(output_file, 'w') as problem_file:
        # Domain definition
        problem_file.write(f"(define (problem {problem_name})\n    (:domain {domain})\n")

        # Objects definition
        problem_file.write("    (:objects\n        ")
        for book in range(test_num_books):
            problem_file.write(f"book{book} ")
        problem_file.write("- book\n        ")
        for month in months:
            problem_file.write(f"{month} ")
        problem_file.write("- month\n")
        problem_file.write("    )\n")

        # Initial state definition
        problem_file.write("    (:init\n")
        for month in range(len(months)):
            problem_file.write(f"        (= (number_month {months[month]}) {month})\n")

        for book in range(test_num_books):

            # Level 3: pages
            if test_level == 3:
                pages = random.randint(min_pages, max_pages)
                problem_file.write(f"        (= (pages book{book}) {pages})\n")

        # Relationships between books
        for predecessor, book in sequential_pairs:
            problem_file.write(f"        (predecessor book{predecessor} book{book})\n")

        for parallel, book in parallel_pairs:
            problem_file.write(f"        (papapapa book{parallel} book{book})\n")

        # Information about read books and books to read
        for book in read_books:
            problem_file.write(f"        (read book{book})\n")

        for book in books_to_read:
            problem_file.write(f"        (to-read book{book})\n")
            
        problem_file.write("    )\n")

        # Metrics: level 3
        if test_level == 3:
            pass
            # problem_file.write("    (:metric minimize (total-pages))\n") ??? esborrar abans d'entregar siusplau

        # Goal state definition
        problem_file.write("    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))\n")
        problem_file.write(")\n")