import networkx as nx
import matplotlib.pyplot as plt
import random
random.seed(42)

class BookGraph:
    def __init__(self, num_books, chance_predecesor_books=0.35, chance_parallel_books=0.35):
        self.graph = nx.DiGraph()
        self.num_books = num_books
        self.chance_predecesor_books = chance_predecesor_books
        self.chance_parallel_books = chance_parallel_books


    def add_sequential_edge(self, from_book, to_book):
        self.graph.add_edge(from_book, to_book, type="predecessor")

    def add_parallel_edge(self, from_book, to_book):
        self.graph.add_edge(from_book, to_book, type="parallel")

    def add_independent_node(self, book):
        self.graph.add_node(book, type="independent")

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        # Group edges by type
        parallel_edges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d['type'] == 'parallel']
        predecessor_edges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d['type'] == 'predecessor']

        # Add edges
        nx.draw_networkx_edges(self.graph, pos, edgelist=parallel_edges, width=8, alpha=0.5, edge_color='r', style='dashed')
        nx.draw_networkx_edges(self.graph, pos, edgelist=predecessor_edges, width=8, alpha=0.5, edge_color='b')

        nx.draw_networkx_nodes(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)
        plt.show()

    def generate_graph(self, level):
        available_books = set(range(self.num_books))
        if level == 0:
            for book in range(self.num_books):
                if random.random() < self.chance_predecesor_books and len(available_books) > 1:
                    predecesor = random.choice(list(available_books - set([book])))
                    self.add_sequential_edge(predecesor, book)
                    available_books.remove(predecesor)
                else:
                    self.add_independent_node(book)
        if level == 1:
            for book in range(self.num_books):
                number_predecesors = round(random.randint(0, len(available_books) - 1) * self.chance_predecesor_books)
                print(number_predecesors)
                predecesors = random.sample(list(available_books - set([book])), number_predecesors)
                for predecesor in predecesors:
                    self.add_sequential_edge(predecesor, book)
                    available_books.remove(predecesor)
                if number_predecesors == 0:
                    self.add_independent_node(book)
        if level > 1:
            for book in range(self.num_books):
                number_predecesors = round(random.randint(0, len(available_books) - 1) * self.chance_predecesor_books)
                number_parallels = round(random.randint(0, len(available_books) - 1) * self.chance_parallel_books)
                predecesors = random.sample(list(available_books - set([book])), number_predecesors)
                parallels = random.sample(list(available_books - set([book]) - set(predecesors)), number_parallels)
                for predecesor in predecesors:
                    self.add_sequential_edge(predecesor, book)
                    available_books.remove(predecesor)
                for parallel in parallels:
                    self.add_parallel_edge(parallel, book)
                    available_books.remove(parallel)
                if number_predecesors == 0 and number_parallels == 0:
                    self.add_independent_node(book)

            

graph = BookGraph(15)
graph.generate_graph(3)
graph.visualize_graph()