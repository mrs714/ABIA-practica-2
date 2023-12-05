import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy


class BookGraph:
    def __init__(self, num_books, random_seed, chance_predecesor_books=0.5, chance_parallel_books=0.3, multi_par = False):
        self.graph = nx.DiGraph()
        self.num_books = num_books
        self.chance_predecesor_books = chance_predecesor_books
        self.chance_parallel_books = chance_parallel_books
        random.seed(random_seed)
        numpy.random.seed(random_seed)
        self.multipar = multi_par

    def add_sequential_edge(self, from_book, to_book):
        self.graph.add_edge(from_book, to_book, type="predecessor")

    def add_parallel_edge(self, from_book, to_book):
        self.graph.add_edge(from_book, to_book, type="parallel")

    def add_independent_node(self, book):
        self.graph.add_node(book, type="independent")
    def remove_edge(self, from_book, to_book):
        self.graph.remove_edge(from_book, to_book)

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph, k=1.6, iterations=200) 
        # Group edges by type
        parallel_edges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d['type'] == 'parallel']
        predecessor_edges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d['type'] == 'predecessor']

        # Add edges
        nx.draw_networkx_edges(self.graph, pos, edgelist=parallel_edges, width=4, alpha=0.5, edge_color='r', style='dashed', arrows = False)
        nx.draw_networkx_edges(self.graph, pos, edgelist=predecessor_edges, width=4, alpha=0.5, edge_color='b')

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
            nx.draw_networkx_nodes(self.graph, pos, nodelist=list(set(self.get_all_nodes()) - set(read_books) - set(books_to_read)), node_color='cyan')

        nx.draw_networkx_labels(self.graph, pos)
        plt.show()

    def generate_graph(self, level):
        self.graph.add_nodes_from(range(self.num_books))
        if level >= 0:
            for j in range(self.num_books):
                if random.random() < self.chance_predecesor_books:
                    available = [x for x in range(self.num_books)]
                    i = random.choice(available)
                    while nx.has_path(self.graph, j, i) and len(available) > 1:
                        available.remove(i)
                        i = random.choice(available)
                    available.remove(i)
                    if len(available)>0 or (len(available) == 0 and not nx.has_path(self.graph, j,i)):
                        self.graph.add_edge(i,j,type="predecessor")
        if level >= 1:
            for j in range(self.num_books):
                for _ in range(random.randint(1, self.num_books)):
                    if random.random() < self.chance_predecesor_books/self.num_books: #less probability of new predecessors
                        available = [x for x in range(self.num_books)]
                        i = random.choice(available)
                        while nx.has_path(self.graph, j, i) and len(available) > 1:
                            available.remove(i)
                            i = random.choice(available)
                        available.remove(i)
                        if len(available)>0 or (len(available) == 0 and not nx.has_path(self.graph, j,i)):
                            self.graph.add_edge(i,j,type="predecessor")
        if level >= 2: # On top of the previous level, add parallel edges
            for _ in range(self.num_books):
                if random.random() < self.chance_parallel_books:
                    if self.multipar:
                        available = [(i,j) for i in range(self.num_books) for j in range(self.num_books)]
                        i, j = random.choice(available)
                        while (nx.has_path(self.graph, i, j) or nx.has_path(self.graph, j, i)) and len(available) > 1:
                            available.remove((i,j))
                            i, j = random.choice(available)
                        available.remove((i,j))
                        if len(available)>0 or (len(available)==0 and (not nx.has_path(self.graph, i, j) and not nx.has_path(self.graph, j, i))):
                            self.graph.add_edge(i, j, type="parallel")
                            self.graph.add_edge(j, i, type="parallel")
                    else:
                        available = [(i,j) for i in range(self.num_books) for j in range(self.num_books)]
                        i, j = random.choice(available)
                        while (nx.has_path(self.graph, i, j) or nx.has_path(self.graph, j, i)) and len(available) > 1:
                            available.remove((i,j))
                            i, j = random.choice(available)
                        available.remove((i,j))

                        n = self.get_parallel_edge_nodes()
                        n = [item for tup in n for item in tup]
                        if (len(available)>0 or (len(available)==0 and (not nx.has_path(self.graph, i, j) and not nx.has_path(self.graph, j, i))))\
                                and i not in n and j not in n:
                            self.graph.add_edge(i, j, type="parallel")
                            self.graph.add_edge(j, i, type="parallel")

    def generate_simplified_graph(self, level):
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
                parallels = random.sample(list(available_parallel_books - set([book]) - set(predecesors)), number_parallels)
                for parallel in parallels:
                    self.add_parallel_edge(parallel, book)
                    available_parallel_books.remove(parallel)
                    if book in available_parallel_books:
                        available_parallel_books.remove(book)
                if number_parallels == 0:
                    self.add_independent_node(book)

    def create_graph_from_selection(self, books = [], predecessors = [], parallels = []):
        self.graph.add_nodes_from(books)
        for e in predecessors:
            self.graph.add_edge(e[0], e[1], type="predecessor")
        for p in parallels:
            self.graph.add_edge(p[0], p[1], type="parallel")
            self.graph.add_edge(p[1], p[0], type="parallel")
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
                if (v,u) not in node_pairs:
                    node_pairs.append((u, v))
        return node_pairs
    def get_all_nodes(self):
        return list(self.graph)

    def make_mistborn(self, level: str):
        # Level: 01, 02 for level 0; 11, 12 for level 1; ...

        total_books = []
        books = ["TheFinalEmpire", "TheWellOfAscension", "TheHeroOfAges"]
        total_books += books
        
        # Relacions sequencials
        for book in range(len(books) - 1):
            self.add_sequential_edge(books[book], books[book + 1])

        books = ["TheAlloyOfLaw", "ShadowsOfSelf", "TheBandsOfMourning", "TheLostMetal"]
        total_books += books

        for book in range(len(books) - 1):
            self.add_sequential_edge(books[book], books[book + 1])

        books = ["TheEleventhMetal", "AllomancerJak", "MistbornSecretHistory"]
        total_books += books

        self.add_sequential_edge("TheHeroOfAges", "MistbornSecretHistory")

        self.add_independent_node("TheEleventhMetal")
        self.add_independent_node("AllomancerJak")

        books = ["TheWayOfKings", "WordsOfRadiance", "Oathbringer", "RhythmOfWar"]
        total_books += books

        for book in range(len(books) - 1):
            self.add_sequential_edge(books[book], books[book + 1])

        books = ["Dawnshard", "Edgedancer", "Horneater"]
        total_books += books

        for book in books:
            self.add_independent_node(book)
        
        read = ["TheAlloyOfLaw", "TheWayOfKings"]
        to_read = ["ShadowsOfSelf", "TheBandsOfMourning", "TheLostMetal"]
        to_read += ["MistbornSecretHistory"]
        to_read += ["RhythmOfWar"]

        if level == "01":
            return
        
        self.add_sequential_edge("Oathbringer", "Dawnshard")
        self.add_sequential_edge("RhythmOfWar", "Horneater")
        books = ["TheStormlightArchive5"]
        total_books += books
        self.add_sequential_edge("RhythmOfWar", "TheStormlightArchive5")
        to_read += ["Dawnshard", "Horneater"]
        
        if level == "02":
            return
        
        books = ["Warbreaker", "Nightblood"]
        total_books += books
        self.add_sequential_edge("Warbreaker", "Nightblood")
        self.add_sequential_edge("Warbreaker", "WordsOfRadiance")
        self.add_sequential_edge("Oathbringer", "MistbornSecretHistory")
        self.add_sequential_edge("TheBandsOfMourning", "MistbornSecretHistory")
        self.add_sequential_edge("TheHeroOfAges", "Oathbringer")
        
        if level == "11":
            return
        
        self.add_sequential_edge("TheHeroOfAges", "TheEleventhMetal")
        self.add_sequential_edge("TheAlloyOfLaw", "AllomancerJak")
        self.add_sequential_edge("WordsOfRadiance", "Edgedancer")
        self.add_sequential_edge("Edgedancer", "Oathbringer")

        if level == "12":
            return
        
        self.remove_edge("Oathbringer", "MistbornSecretHistory")
        self.add_parallel_edge("Oathbringer", "Mistborn: Secret History")
        self.remove_edge("Warbreaker", "WordsOf Radiance")
        self.add_parallel_edge("Warbreaker", "WordsOf Radiance")

        if level == "21":
            return
        
        self.remove_edge("TheHeroOfAges", "MistbornSecretHistory")
        self.add_parallel_edge("TheHeroOfAges", "MistbornSecretHistory")  

        if level == "22":
            return
        

# Test
"""
graph = BookGraph(15,42)
graph.generate_graph(3)
graph.visualize_graph()
print(graph.get_parallel_edge_nodes(), graph.get_sequetial_edge_nodes())
"""

# Creation of graphs for manual testing:
# BookGraph(0,0,0,0).make_mistborn("22")