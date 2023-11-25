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

    def paint_reading_plan(self, read_books, books_to_read, rest_of_books = []):

        # Visualize the graph, painting the read books in green and the books to read in red
        pos = nx.spring_layout(self.graph, k=1.6, iterations=200) # k = distance between nodes, iterations = number of iterations of the spring layout algorithm
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
        if rest_of_books:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=rest_of_books, node_color='cyan')
        else:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=list(set(range(self.num_books)) - set(read_books) - set(books_to_read)), node_color='cyan')

        nx.draw_networkx_labels(self.graph, pos)
        plt.show()

    def generate_graph(self, level):
        available_books = set(range(self.num_books))
        if level == 0:
            for book in range(self.num_books):
                # Check if book already is a predecesor of another book
                if book in available_books:
                    if random.random() < self.chance_predecesor_books and len(available_books) > 1:
                        predecesor = random.choice(list(available_books - set([book])))
                        self.add_sequential_edge(predecesor, book)
                        available_books.remove(predecesor)
                    else:
                        self.add_independent_node(book)
                else:
                    self.add_independent_node(book)
        if level > 0:
            for book in range(self.num_books):
                # Assign a random number of predecesors to the book, balanced depending on the number of available books
                number_predecesors = round(random.randint(0, len(available_books) - 1) * (self.chance_predecesor_books - (self.chance_predecesor_books * (len(available_books) / self.num_books))/1.1))
                predecesors = random.sample(list(available_books - set([book])), number_predecesors )
                for predecesor in predecesors:
                    self.add_sequential_edge(predecesor, book)
                    available_books.remove(predecesor)
                if number_predecesors == 0:
                    self.add_independent_node(book)
        if level > 1: # On top of the previous level, add parallel edges
            available_parallel_books = set(range(self.num_books))
            for book in range(self.num_books):
                # Assign a random number of predecesors and parallels to the book, balanced depending on the number of available books
                number_parallels = round(random.randint(0, len(available_parallel_books) - 1) * (self.chance_parallel_books - (self.chance_parallel_books * (len(available_parallel_books) / self.num_books))/1.5))
                if number_parallels == 0:
                    number_parallels = 1 if random.random() < self.chance_parallel_books  else 0
                    print(number_parallels)
                parallels = random.sample(list(available_parallel_books - set([book]) - set(predecesors)), number_parallels)
                for parallel in parallels:
                    self.add_parallel_edge(parallel, book)
                    available_parallel_books.remove(parallel)
                    if book in available_parallel_books:
                        available_parallel_books.remove(book)
                if number_parallels == 0:
                    self.add_independent_node(book)
        
    def get_sequetial_edge_nodes(self):
        # Returns all pairs of nodes that are connected by a sequential edge
        node_pairs = []
        for (u, v, d) in self.graph.edges(data=True):
            if d['type'] == 'predecessor':
                node_pairs.append((u, v))
        return node_pairs

    def get_parallel_edge_nodes(self):
        # Returns all pairs of nodes that are connected by a parallel edge
        node_pairs = []
        for (u, v, d) in self.graph.edges(data=True):
            if d['type'] == 'parallel':
                node_pairs.append((u, v))
        return node_pairs
    
    def make_mistborn(self, level: str):
        # Level: 01, 02 for level 0; 11, 12 for level 1; ...

        total_books = []
        books = ["The Final Empire", "The Well of Ascension", "The Hero of Ages"]
        total_books += books
        
        # Relacions sequencials
        for book in range(len(books) - 1):
            self.add_sequential_edge(books[book], books[book + 1])

        books = ["The Alloy of Law", "Shadows of Self", "The Bands of Mourning", "The Lost Metal"]
        total_books += books

        for book in range(len(books) - 1):
            self.add_sequential_edge(books[book], books[book + 1])

        books = ["The Eleventh Metal", "Allomancer Jak", "Mistborn: Secret History"]
        total_books += books

        self.add_sequential_edge("The Hero of Ages", "Mistborn: Secret History")

        self.add_independent_node("The Eleventh Metal")
        self.add_independent_node("Allomancer Jak")

        books = ["The Way of Kings", "Words of Radiance", "Oathbringer", "Rhythm of War"]
        total_books += books

        for book in range(len(books) - 1):
            self.add_sequential_edge(books[book], books[book + 1])

        books = ["Dawnshard", "Edgedancer", "Horneater"]
        total_books += books

        for book in books:
            self.add_independent_node(book)
        
        read = ["The Alloy of Law", "The Way of Kings"]
        to_read = ["Shadows of Self", "The Bands of Mourning", "The Lost Metal"]
        to_read += ["Mistborn: Secret History"]
        to_read += ["Rhythm of War"]

        if level == "01":
            self.paint_reading_plan(read, to_read, list(set(total_books) - set(read) - set(to_read)))
            return
        
        self.add_sequential_edge("Oathbringer", "Dawnshard")
        self.add_sequential_edge("Rhythm of War", "Horneater")
        books = ["The Stormlight Archive 5"]
        total_books += books
        self.add_sequential_edge("Rhythm of War", "The Stormlight Archive 5")
        to_read += ["Dawnshard", "Horneater"]
        
        if level == "02":
            self.paint_reading_plan(read, to_read, list(set(total_books) - set(read) - set(to_read)))
            return
        
        books = ["Warbreaker", "Nightblood"]
        total_books += books
        self.add_sequential_edge("Warbreaker", "Nightblood")
        self.add_sequential_edge("Warbreaker", "Words of Radiance")
        self.add_sequential_edge("Oathbringer", "Mistborn: Secret History")
        self.add_sequential_edge("The Bands of Mourning", "Mistborn: Secret History")
        self.add_sequential_edge("The Hero of Ages", "Oathbringer")
        
        if level == "03":
            self.paint_reading_plan(read, to_read, list(set(total_books) - set(read) - set(to_read)))
            return
        
        self.add_sequential_edge("The Hero of Ages", "The Eleventh Metal")
        self.add_sequential_edge("The Alloy of Law", "Allomancer Jak")
        self.add_sequential_edge("Words of Radiance", "Edgedancer")
        self.add_sequential_edge("Edgedancer", "Oathbringer")

        if level == "04":
            self.paint_reading_plan(read, to_read, list(set(total_books) - set(read) - set(to_read)))
            return
        



 
#BookGraph(0,0,0,0).make_mistborn("04")
# Test
"""
graph = BookGraph(15,42)
graph.generate_graph(3)
graph.visualize_graph()
print(graph.get_parallel_edge_nodes(), graph.get_sequetial_edge_nodes())
"""