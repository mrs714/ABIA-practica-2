import subprocess
import os
import random
from graph_generator import BookGraph
import numpy
import time
import csv
import platform
class BookGraphGenerator:
    def __init__(self, num_books, level=3, domain="books", predecessor_chance=0.4,
                 parallel_chance=0.2, read_books_percentage=0.2,
                 books_to_read_percentage=0.3, random_seed=42,
                 sequential_program=True, results=True, show_graph = False):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.show_graph = show_graph
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
        sequen = "sequencial_" if sequential_program else ""
        level = level if level != 0 else "basic"
        self.domain_file = f"./FitxersPDDL/Domini_{sequen}{level}.pddl"
        self.time = "Not recorded"
        self.results = results
        self.pages = None
        self.cosmere = False

    def generate_book_graph(self, simplified=False):
        self.problem_name = f"test{self.num_books}-{self.level}"
        self.problem_name_path = self.problem_name + ".pddl"
        self.output_file = os.path.join(self.script_dir, self.problem_name_path)
        self.max_pages = min(8000 // self.num_books, 800)
        self.min_pages = self.max_pages // 2
        self.graph = BookGraph(num_books=self.num_books, random_seed=self.random_seed, chance_predecesor_books=self.predecessor_chance, chance_parallel_books=self.parallel_chance)
        if not simplified:
            self.graph.generate_graph(self.level)
        else:
            self.graph.generate_simplified_graph(self.level)
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

    def book_graph_from_selection(self, books, predecessors, parallels, pages = [], read = [], to_read = []):
        self.problem_name = f"test{self.num_books}-{self.level}"
        self.problem_name_path = self.problem_name + ".pddl"
        self.output_file = os.path.join(self.script_dir, self.problem_name_path)
        self.max_pages = min(8000 // len(books), 800)
        self.min_pages = self.max_pages // 2
        self.graph = BookGraph(num_books=self.num_books, random_seed=self.random_seed, chance_predecesor_books=self.predecessor_chance, chance_parallel_books=self.parallel_chance)
        self.graph.create_graph_from_selection(books, predecessors, parallels)
        self.sequentials = self.graph.get_sequetial_edge_nodes()
        self.parallels = self.graph.get_parallel_edge_nodes()
        self.others = list(set(self.graph.get_all_nodes()) - set(self.sequentials) - set(self.parallels))
        self.pages = pages
        self.all_books = self.graph.get_all_nodes()
        self.sequential_books = set(i for i, j in self.sequentials).union(set(j for i, j in self.sequentials))
        self.parallel_books = set(i for i, j in self.parallels).union(set(j for i, j in self.parallels))
        self.normal_books = list(set(self.all_books) - self.sequential_books - self.parallel_books)

        self.available_books = self.all_books
        self.read_books = read
        self.available_books = list(set(self.available_books) - set(self.read_books))
        self.books_to_read = to_read
        self.available_books = list(set(self.available_books) - set(self.books_to_read))

        print(f"Test {self.problem_name}: {self.num_books} books, {len(self.sequentials)} sequential pairs, {len(self.parallels)} parallel pairs, {len(self.read_books)} read books, {len(self.books_to_read)} books to read")
        if self.show_graph:
            self.graph.paint_reading_plan(self.read_books, self.books_to_read)
    
    def save_results(self):
        if not self.cosmere:
            results_path = "".join([self.script_dir, "/", "results",self.problem_name, ".txt"])
        else:
            results_path = "".join([self.script_dir, "/", "ResultsJocDeProva",self.problem_name, ".txt"])
        with open(results_path, 'w') as fp:
            for item in self.assignations:
                # write each item on a new line
                fp.write("%s\n" % str(item))
            fp.write(f"Execution time: {self.time:.2f} seconds")
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
            problem_file.write("        (= (monthnum) 0)\n")
            for month in range(len(self.months)):
                problem_file.write(f"        (= (number_month {self.months[month]}) {month})\n")

            for book in range(len(self.all_books)):
                # Level 3: pages
                if self.level == 3:
                    if self.pages == None:
                        pages = random.randint(self.min_pages, self.max_pages)
                    else:
                        print(self.pages)
                        print(book)
                        print(self.all_books)
                        pages = self.pages[book]
                    problem_file.write(f"        (= (pages book{self.all_books[book]}) {pages})\n")

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

    def cosmere_test(self, clevel):
        self.cosmere = True
        self.problem_name = f"JocDeProva-{clevel}"
        self.problem_name_path = self.problem_name + ".pddl"
        self.output_file = os.path.join(self.script_dir, self.problem_name_path)
        self.graph = BookGraph(num_books=self.num_books, random_seed=self.random_seed, chance_predecesor_books=self.predecessor_chance, chance_parallel_books=self.parallel_chance)
        self.graph.make_mistborn(clevel)
        self.sequentials = self.graph.get_sequetial_edge_nodes()
        self.parallels = self.graph.get_parallel_edge_nodes()
        self.others = list(set(self.graph.get_all_nodes()) - set(self.sequentials) - set(self.parallels))

        self.all_books = self.graph.get_all_nodes()
        

        print(self.all_books)
        self.sequential_books = set(i for i, j in self.sequentials).union(set(j for i, j in self.sequentials))
        self.parallel_books = set(i for i, j in self.parallels).union(set(j for i, j in self.parallels))
        self.normal_books = list(set(self.all_books) - self.sequential_books - self.parallel_books)

        self.available_books = self.all_books
        self.read_books = set(random.sample(self.available_books, int(self.num_books * self.read_books_percentage)))
        self.available_books = list(set(self.available_books) - self.read_books)
        self.books_to_read = set(random.sample(self.available_books, int(self.num_books * self.books_to_read_percentage)))
        self.available_books = list(set(self.available_books) - self.books_to_read)

        print(f"Test {self.problem_name}: {len(self.all_books)} books, {len(self.sequentials)} sequential pairs, {len(self.parallels)} parallel pairs, {len(self.read_books)} read books, {len(self.books_to_read)} books to read")
        if self.show_graph:
            self.graph.paint_reading_plan(self.read_books, self.books_to_read)

        
        

    def run_metricff(self, maxtime = 20):
        start_time = time.time()
        if platform.system() == "Linux":
            exec_file = "./FitxersPDDL/ff"
        elif platform.system() == "Darwin":
            exec_file = "./FitxersPDDL/ff"
        else:
            exec_file = "./FitxersPDDL/metricff.exe"
        
        process = subprocess.Popen([exec_file, "-o", self.domain_file, "-f", f"./JocsDeProva/{self.problem_name}.pddl"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            stdout, stderr = process.communicate(timeout=maxtime)
        except:
            process.terminate()      
            self.assignations.append(f"This problem couldn't be solved in less than {maxtime} seconds.")
            self.time = 20
            if self.results == True:
                self.save_results()
            return 999
            
        end_time = time.time()
        out = stdout.decode("utf-8")
        output_lines = out.split("\n")
        
        output_lines = [o.lstrip() for o in output_lines]
        self.time = end_time - start_time
        if "ff: found legal plan as follows" in output_lines:
            
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
            
            if self.results == True:
                self.save_results()
            return self.time
        return self.time
    def get_results(self):
        return self.assignations

            
"""
generator = BookGraphGenerator(num_books=books_num[b], level = levels[b], random_seed= seed, results=True, sequential_program=sequential)
generator.generate_book_graph()
generator.write_pddl_file()
exectime = generator.run_metricff()

"""


def sequence_of_experiments( experiment_name = "", books_num = [], levels = [], predecessor_chances = [], parallel_chances = [], read_books_percentages = [], books_to_read_percentages = [], sequentials=[False],seeds= [], append = False):
    output_file = f"./experiment-{experiment_name}.csv"
    if not append:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Sequential", "BooksNumber", "Time", "Seed"])
            file.close()
    for seed in seeds:
        print(seed)
        for b in range(len(books_num)):
            for sequential in sequentials:
                generator = BookGraphGenerator(num_books=books_num[b], level = levels[b], random_seed= seed, results=True, sequential_program=sequential)
                generator.generate_book_graph()
                generator.write_pddl_file()
                time = generator.run_metricff()
                with open(output_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([sequential, books_num[b], time, seed])


if __name__ == '__main__':
    experiments = ["basic", "extensio1", "extensio2", "extensio3"]
    nivells = [0,1,2,3]
    books_list = range(25,35)


    generator = BookGraphGenerator(num_books=25, level = 0, random_seed= 42, results=True, sequential_program=True, show_graph=True)
    generator.cosmere_test("01")
    generator.write_pddl_file()
    timer = generator.run_metricff()
    print(timer)
    for e in range(len(experiments)):
        name = experiments[e]
        #sequence_of_experiments(name, books_num=books_list, levels = [nivells[e] for _ in range(len(books_list))], sequentials=[False,True], seeds = [42,10, 249, 145], append=True)