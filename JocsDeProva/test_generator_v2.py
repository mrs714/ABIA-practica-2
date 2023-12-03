import os
import random
from graph_generator import BookGraph

# Get the directory of the currently executing script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Wether to show the book graph when creating each test
show_graph = True
level = 3
num_books = 15
domain = "books"
predecessor_chance = 0.5
parallel_chance = 0.3
read_books_percentage = 0.3
books_to_read_percentage = 0.3
random_seed = 42
sequential_program = True
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
random.seed(random_seed)




problem_name = "test"+str(num_books)+"-"+str(level)
problem_name_path = problem_name + ".pddl"
output_file = os.path.join(script_dir, problem_name_path)
max_pages = min(5000//num_books, 800)
min_pages = max_pages//2
graph = BookGraph(num_books=num_books, random_seed=random_seed, chance_predecesor_books=predecessor_chance, chance_parallel_books=parallel_chance)
graph.generate_graph(level)

sequentials = graph.get_sequetial_edge_nodes()
parallels = graph.get_parallel_edge_nodes()
others = list(set(graph.get_all_nodes()) - set(sequentials) - set(parallels))

all_books = graph.get_all_nodes()
sequential_books = set(i for i,j in sequentials).union(set(j for i,j in sequentials))
parallel_books = set(i for i,j in parallels).union(set(j for i,j in parallels))
normal_books = list(set(all_books) - sequential_books - parallel_books)


available_books = all_books
read_books = set(random.sample(available_books, int(num_books*read_books_percentage)))
available_books = list(set(available_books) - read_books)
books_to_read = set(random.sample(available_books, int(num_books*books_to_read_percentage)))
available_books = list(set(available_books) - books_to_read)

print(f"Test {problem_name}: {num_books} books, {len(sequentials)} sequential pairs, {len(parallels)} parallel pairs, {len(read_books)} read books, {len(books_to_read)} books to read")
if show_graph:
    graph.paint_reading_plan(read_books, books_to_read)

with open(output_file, 'w') as problem_file:
    # Domain definition
    problem_file.write(f"(define (problem {problem_name})\n    (:domain {domain})\n")

    # Objects definition - Basic and 1 don't have subtypes, 2 and 3 do
    problem_file.write("    (:objects\n        ")
    if level == 0 or level == 1 or sequential_program == True:
        for book in all_books:
            problem_file.write(f"book{book} ")
        problem_file.write("- book\n        ")
    else:
        if normal_books:
            for book in normal_books:
                problem_file.write(f"book{book} ")
            problem_file.write("- book\n        ")
        if sequential_books:
            for book in sequential_books:
                problem_file.write(f"book{book} ")
            problem_file.write("- predecessor_book\n        ")
        if parallel_books:
            for book in parallel_books:
                problem_file.write(f"book{book} ")
            problem_file.write("- parallel_book\n        ")

    # Objects: months
    for month in months:
        problem_file.write(f"{month} ")
    problem_file.write("- month\n")
    problem_file.write("    )\n")

    # Initial state definition
    problem_file.write("    (:init\n")
    if sequential_program:
        problem_file.write("        (= (monthnum) 0)\n")
    for month in range(len(months)):
        problem_file.write(f"        (= (number_month {months[month]}) {month})\n")

    for book in all_books:
        # Level 3: pages
        if level == 3:
            pages = random.randint(min_pages, max_pages)
            problem_file.write(f"        (= (pages book{book}) {pages})\n")

    # Relationships between books
    for predecessor, book in sequentials:
        problem_file.write(f"        (predecessor book{predecessor} book{book})\n")

    for parallel, book in parallels:
        problem_file.write(f"        (parallel book{parallel} book{book})\n")

    # Information about read books and books to read
    for book in read_books:
        problem_file.write(f"        (read book{book})\n")

    for book in books_to_read:
        problem_file.write(f"        (to-read book{book})\n")

    if level == 3:
        for month in months:
            problem_file.write(f"        (= (month_pages {month}) 0)\n")
        problem_file.write(f"        (= (maxpages) 800)\n")
    
    problem_file.write("    )\n")
    # Goal state definition
    problem_file.write("    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))\n")
    problem_file.write(")\n")