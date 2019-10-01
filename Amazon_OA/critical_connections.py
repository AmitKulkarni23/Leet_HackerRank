# # https://leetcode.com/discuss/interview-question/372581 Given an underected connected graph with n nodes labeled
# 1..n. A bridge (cut edge) is defined as an edge which, when removed, makes the graph disconnected (or more
# precisely, increases the number of connected components in the graph). Equivalently, an edge is a bridge if and
# only if it is not contained in any cycle. The task is to find all bridges in the given graph. Output an empty list
# if there are no bridges.
#
# Input:
#
# n, an int representing the total number of nodes.
# edges, a list of pairs of integers representing the nodes connected by an edge.

# Solution - Targjan's algorithm to find strongly connected components

# Basic Idea:
# Low link Values - is the smallest node ID reachable from that node(when doig a dfs) including itself.
# All nodes that have the same low link value belong to the same SCC
# But, this is highly dependent on DFS. DFS can choose any path
# During the callback of the dfs, we update the lowlink values.


# Time Complexity -> O(V + E)
# Space Complexity -> O(V + E)

import collections


class Bridges:
    def __init__(self):
        self.ids = None
        self.low = None
        self.id = None
        self.graph = None

    def build_graph(self, edges):
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def visit(self, at, parent, bridges):
        self.low[at] = self.ids[at] = self.id
        self.id += 1

        for to in self.graph[at]:
            if to == parent:
                continue
            if self.ids[to] == 0:
                # This is not visited yet
                self.visit(to, at, bridges)

                # Callback
                self.low[at] = min(self.low[at], self.low[to])

                # This is a bridge edge
                if self.ids[at] < self.low[to]:
                    bridges.append([at, to])

            else:
                self.low[at] = min(self.low[at], self.low[to])

    def find_bridges(self, num_nodes, edges):
        bridges = []
        self.graph = self.build_graph(edges)
        self.id = 1
        self.ids = [0] * (num_nodes + 1)
        self.low = [0] * (num_nodes + 1)

        self.visit(1, -1, bridges)
        return bridges


bridge_obj = Bridges()
n = 5
edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]

# n = 6
# edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]

# n = 9
# edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]

print(bridge_obj.find_bridges(n, edges))
