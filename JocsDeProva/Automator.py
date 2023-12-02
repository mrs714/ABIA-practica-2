import subprocess
import os
import random
from graph_generator import BookGraph
import numpy

class BookGraphGenerator:
    def __init__(self, num_books, level=3, domain="books", predecessor_chance=0.5,
                 parallel_chance=0.3, read_books_percentage=0.3,
                 books_to_read_percentage=0.3, random_seed=42,
                 sequential_program=True):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.show_graph = True
        self.num_books = num_books
        self.level = level
        self.domain = domain
        self.predecessor_chance = predecessor_chance
        self.parallel_chance = parallel_chance
        self.read_books_percentage = read_books_percentage
        self.books_to_read_percentage = books_to_read_percentage
        self.random_seed = random_seed
        self.sequential_program = sequential_program
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        random.seed(random_seed)
        numpy.random.seed(random_seed)
        self.assignations = []

    def generate_book_graph(self):
        self.problem_name = f"test{self.num_books}-{self.level}"
        self.problem_name_path = self.problem_name + ".pddl"
        self.output_file = os.path.join(self.script_dir, self.problem_name_path)
        self.max_pages = min(5000 // self.num_books, 800)
        self.min_pages = self.max_pages // 2
        self.graph = BookGraph(num_books=self.num_books, random_seed=self.random_seed, chance_predecesor_books=self.predecessor_chance, chance_parallel_books=self.parallel_chance)
        self.graph.generate_graph(self.level)

        self.sequentials = self.graph.get_sequetial_edge_nodes()
        self.parallels = self.graph.get_parallel_edge_nodes()
        self.others = list(set(self.graph.get_all_nodes()) - set(self.sequentials) - set(self.parallels))

        self.all_books = self.graph.get_all_nodes()
        self.sequential_books = set(i for i, j in self.sequentials).union(set(j for i, j in self.sequentials))
        self.parallel_books = set(i for i, j in self.parallels).union(set(j for i, j in self.parallels))
        self.normal_books = list(set(self.all_books) - self.sequential_books - self.parallel_books)

        self.available_books = self.all_books
        self.read_books = set(random.sample(self.available_books, int(self.num_books * self.read_books_percentage)))
        self.available_books = list(set(self.available_books) - self.read_books)
        self.books_to_read = set(random.sample(self.available_books, int(self.num_books * self.books_to_read_percentage)))
        self.available_books = list(set(self.available_books) - self.books_to_read)

        print(f"Test {self.problem_name}: {self.num_books} books, {len(self.sequentials)} sequential pairs, {len(self.parallels)} parallel pairs, {len(self.read_books)} read books, {len(self.books_to_read)} books to read")
        if self.show_graph:
            self.graph.paint_reading_plan(self.read_books, self.books_to_read)

    def write_pddl_file(self):
        with open(self.output_file, 'w') as problem_file:
            # Domain definition
            problem_file.write(f"(define (problem {self.problem_name})\n    (:domain {self.domain})\n")

            # Objects definition
            problem_file.write("    (:objects\n        ")
            if self.level == 0 or self.level == 1 or self.sequential_program:
                for book in self.all_books:
                    problem_file.write(f"book{book} ")
                problem_file.write("- book\n        ")
            else:
                if self.normal_books:
                    for book in self.normal_books:
                        problem_file.write(f"book{book} ")
                    problem_file.write("- book\n        ")
                if self.sequential_books:
                    for book in self.sequential_books:
                        problem_file.write(f"book{book} ")
                    problem_file.write("- predecessor_book\n        ")
                if self.parallel_books:
                    for book in self.parallel_books:
                        problem_file.write(f"book{book} ")
                    problem_file.write("- parallel_book\n        ")

            # Objects: months
            for month in self.months:
                problem_file.write(f"{month} ")
            problem_file.write("- month\n")
            problem_file.write("    )\n")

            # Initial state definition
            problem_file.write("    (:init\n")
            if self.sequential_program:
                problem_file.write("        (= (monthnum) 0)\n")
            for month in range(len(self.months)):
                problem_file.write(f"        (= (number_month {self.months[month]}) {month})\n")

            for book in self.all_books:
                # Level 3: pages
                if self.level == 3:
                    pages = random.randint(self.min_pages, self.max_pages)
                    problem_file.write(f"        (= (pages book{book}) {pages})\n")

            # Relationships between books
            for predecessor, book in self.sequentials:
                problem_file.write(f"        (predecessor book{predecessor} book{book})\n")

            for parallel, book in self.parallels:
                problem_file.write(f"        (parallel book{parallel} book{book})\n")

            # Information about read books and books to read
            for book in self.read_books:
                problem_file.write(f"        (read book{book})\n")

            for book in self.books_to_read:
                problem_file.write(f"        (to-read book{book})\n")

            if self.level == 3:
                for month in self.months:
                    problem_file.write(f"        (= (month_pages {month}) 0)\n")
                problem_file.write(f"        (= (maxpages) 800)\n")

            problem_file.write("    )\n")
            # Goal state definition
            problem_file.write("    (:goal (forall (?book - book) (imply (to-read ?book) (read ?book))))\n")
            problem_file.write(")\n")

    def run_metricff(self):
        exec = subprocess.run(["./FitxersPDDL/metricff.exe", "-o", ".\FitxersPDDL\Domini_sequencial_3.pddl", "-f", f"./JocsDeProva/{self.problem_name}.pddl"], capture_output=True)
        out = str(exec.stdout)
        output_lines = out.split("\\n")
        output_lines = [o.lstrip() for o in output_lines]
        start_line = output_lines.index("ff: found legal plan as follows") + 1
        print("Steps taken:")
        for line in output_lines[start_line:]:
            if "REACH-GOAL" in line:
                break
            if line.startswith("step"):
                line = (line.strip("step")).lstrip()
            if "ASSIGN_TO_MONTH" in line:
                a = line.split(" ")
                self.assignations.append((a[2], a[3]))
            print(line)
        print(self.assignations)

# Example usage:
generator = BookGraphGenerator(num_books=15, level=3, random_seed=10)
generator.generate_book_graph()
generator.write_pddl_file()
generator.run_metricff()
