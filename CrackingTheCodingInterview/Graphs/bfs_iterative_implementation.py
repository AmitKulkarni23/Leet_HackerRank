# Python file which demonstrates an implentation of the BFS algorithm

# Data structure used :Queue

# The graph class
class Graph:

    # The constructor
    def __init__(self, V):
        """
        The constructor for this class
        V -> represents the number of vertices in the graph
        """
        self.V = V

        # The adjacencey list
        self.adj_list = {}


    def add_edge(self, v, w):
        """
        Function that adds edge (v, w)
        """
        if v in self.adj_list:
            self.adj_list[v].append(w)
        else:
            self.adj_list[v] = [w]


    def bfs(self, start_node):
        """
        Function that actually implements BFS
        """

        # We will be using a list as a queue

        # Create a boolean array called visited, where visited[i] represents
        # whether node i is visited or not

        # Initially everything in this array is False
        visited_arr = [False] * self.V

        queue = []

        # Add the starting node to the queue
        queue.append(start_node)

        # Now iterate
        while len(queue):

            # Deque this element
            first_node = queue.pop(0)

            # visit this node
            if visited_arr[first_node] == False:
                print("Visiting node ", first_node)
                visited_arr[first_node] = True


            # Get all the adjacent node
            if first_node in self.adj_list:
                for adj_node in self.adj_list[first_node]:
                    if visited_arr[adj_node] == False:
                        queue.append(adj_node)


# Examples
my_graph = Graph(6)
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 5)
my_graph.add_edge(0, 4)
my_graph.add_edge(1, 4)
my_graph.add_edge(1, 3)
my_graph.add_edge(3, 4)
my_graph.add_edge(3, 2)
my_graph.add_edge(2, 1)

my_graph.bfs(0)
