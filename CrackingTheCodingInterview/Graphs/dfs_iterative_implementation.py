# Python file that implements an iterative version of the DFS algorithm
# Uses stack

class Graph:

    # The constructor
    def __init__(self, V):
        """
        Constructor
        v -> is the number of adjacent vertices
        """

        # V represent sthe number of vertices
        # Why do we nede V?
        # We will be using a boolean list o represent whether a node has been
        # visited or not
        # So we need to know the total number of nodes in a graph
        self.V = V

        # Create an adjacency list in the form of dictionary for
        # this particular node

        self.adj_list = {}

    def add_edge(self, v, w):
        """
        Function to add an edge (v, w)
        """

        if v in self.adj_list:
            self.adj_list[v].append(w)
        else:
            self.adj_list[v] = [w]


    def dfs(self, start_node):
        """
        Function that actually performs DFS
        We will emulate teh stack data structure using a python list
        """
        # print("The adjacency list is ", self.adj_list)

        # Created a list to represnt whether
        visited_arr = [False] * self.V

        stack = []

        # Append the start node to stack
        stack.append(start_node)

        # Iterate until the stack is not empty
        while len(stack):

            # get the top node from the stack
            top_node = stack[-1]

            # Pop this top node
            stack.pop()

            # If item is not visited then we print the item
            if visited_arr[top_node] == False:
                # This node has never been visited
                # Therefore visit this node
                print("Visiting node ", top_node)
                visited_arr[top_node] = True


            # Now get all the adjacent elements of the top_node and push it
            # to the stack
            # Why the if condition below?
            # We need to check if there is an outward edge going out from this node
            if top_node in self.adj_list:
                for adj_node in self.adj_list[top_node]:
                    if not visited_arr[adj_node]:
                        stack.append(adj_node)



# Examples
# Create a new graph

my_graph = Graph(5)
my_graph.add_edge(1, 0)
my_graph.add_edge(0, 2)
my_graph.add_edge(2, 1)
my_graph.add_edge(0, 3)
my_graph.add_edge(1, 4)

my_graph.dfs(0)
