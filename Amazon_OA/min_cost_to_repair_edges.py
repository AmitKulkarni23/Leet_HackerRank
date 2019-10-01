from collections import defaultdict
import heapq

# https://leetcode.com/discuss/interview-question/357310
# Solution Credits -> user debeshindia

# Prim's Algorithm -> O((V+E)*logV) because each vertex is inserted in the
# priority queue only once and insertion in priority queue take logarithmic time.

# At each stage maintain the set T of nodes in the tree, and for each node not in the
# tree maintain the least distance from that node to any node in the tree.

# Maintain two disjoint sets of vertices. One containing vertices that are in the growing spanning tree and other
# that are not in the growing spanning tree.
#
# Select the cheapest vertex that is connected to the growing spanning
# tree and is not in the growing spanning tree and add it into the growing spanning tree. This can be done using
# Priority Queues.
#
# Insert the vertices, that are connected to growing spanning tree, into the Priority Queue. Check
# for cycles. To do that, mark the nodes which have been already selected and insert only those nodes in the Priority
# Queue that are not marked.


class Solution:
    def __init__(self):
        pass

    def minCostForRepair(self, n, edges, edgesToRepair):
        graph = defaultdict(list)
        # Graph will be of the form
        # Python's heapq sorts based on the first item in the tuple
        # { u : [(cost_to_repair_u_v1, v1), (cost_to_repair_u_v2, v2)




        broken_edges = set()
        for u, v, cost in edgesToRepair:
            graph[u].append((cost, v))
            graph[v].append((cost, u))
            broken_edges.add((u, v))
            broken_edges.add((v, u))

        for u, v in edges:
            if (u, v) not in broken_edges:
                graph[u].append((0, v))
                graph[v].append((0, u))

        res = 0
        priorityQueue = [(0, 1)]
        heapq.heapify(priorityQueue)

        # We use a set to avoid cycles while adding nodes to the MST
        visited = set()

        while priorityQueue:
            minCost, node = heapq.heappop(priorityQueue)
            if node not in visited:
                visited.add(node)
                res += minCost
                for cost, connectedNode in graph[node]:
                    if connectedNode not in visited:
                        heapq.heappush(priorityQueue, (cost, connectedNode))

        return res


s = Solution()

print(s.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))

print(s.minCostForRepair(6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))