import networkx as nx
import matplotlib.pyplot as plt
import random


class BookGraph:
    def __init__(self, num_books, random_seed, chance_predecesor_books, chance_parallel_books):
        self.graph = nx.DiGraph()
        self.num_books = num_books
        self.chance_predecesor_books = chance_predecesor_books
        self.chance_parallel_books = chance_parallel_books
        random.seed(random_seed)

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

    def paint_reading_plan(self, read_books, books_to_read):
        # Visualize the graph, painting the read books in green and the books to read in red
        pos = nx.spring_layout(self.graph)
        # Group edges by type
        parallel_edges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d['type'] == 'parallel']
        predecessor_edges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d['type'] == 'predecessor']

        # Add edges
        nx.draw_networkx_edges(self.graph, pos, edgelist=parallel_edges, width=8, alpha=0.5, edge_color='r', style='dashed')
        nx.draw_networkx_edges(self.graph, pos, edgelist=predecessor_edges, width=8, alpha=0.5, edge_color='b')

        # Paint the read books in green
        nx.draw_networkx_nodes(self.graph, pos, nodelist=read_books, node_color='g')
        # Paint the books to read in red
        nx.draw_networkx_nodes(self.graph, pos, nodelist=books_to_read, node_color='r')

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
                number_predecesors = round(random.randint(0, len(available_books) - 1) * (self.chance_predecesor_books - (self.chance_predecesor_books * (len(available_books) / self.num_books))/1.1))
                predecesors = random.sample(list(available_books - set([book])), number_predecesors )
                for predecesor in predecesors:
                    self.add_sequential_edge(predecesor, book)
                    available_books.remove(predecesor)
                if number_predecesors == 0:
                    self.add_independent_node(book)
        if level > 1:
            for book in range(self.num_books):
                number_predecesors = round(random.randint(0, len(available_books) - 1) * (self.chance_predecesor_books - (self.chance_predecesor_books * (len(available_books) / self.num_books))/1.1))
                number_parallels = round(random.randint(0, len(available_books) - 1) * (self.chance_parallel_books - (self.chance_parallel_books * (len(available_books) / self.num_books))/1.1))
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
        
    def get_sequetial_edge_nodes(self):
        node_pairs = []
        for (u, v, d) in self.graph.edges(data=True):
            if d['type'] == 'predecessor':
                node_pairs.append((u, v))
        return node_pairs

    def get_parallel_edge_nodes(self):
        node_pairs = []
        for (u, v, d) in self.graph.edges(data=True):
            if d['type'] == 'parallel':
                node_pairs.append((u, v))
        return node_pairs
 
# Test
"""
graph = BookGraph(15,42)
graph.generate_graph(3)
graph.visualize_graph()
print(graph.get_parallel_edge_nodes(), graph.get_sequetial_edge_nodes())
"""