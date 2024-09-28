# https://leetcode.com/problems/find-center-of-star-graph/description/

class Solution:
    def findCenter(self, edges):
        # Space: O(1)
        # Time: O(1)
        # It is guaranteed the center of the graph exists
        # This means that one node should be present in all edges
        # So, the common node in all the edges is the center of teh graph
        # To find the common node, you only need to check the first 2 items in the edges(list of list)
        # Credits - https://leetcode.com/problems/find-center-of-star-graph/editorial/
        
        first_edge, second_edge = edges[0], edges[1]
        return first_edge[0] if first_edge[0] in second_edge else first_edge[1]


    def findCenterMySol(self, edges):
        # Space: O(n) - for center_graph_dict
        # Time: O(n)
        # where n is the number of nodes in the graph
        center_graph_dict = {}
        
        for u, v in edges:
            if u not in center_graph_dict:
                center_graph_dict[u] = 1
            else:
                center_graph_dict[u] += 1

            if v not in center_graph_dict:
                center_graph_dict[v] = 1
            else:
                center_graph_dict[v] += 1

        n = len(edges)
        for item in center_graph_dict:
            if center_graph_dict[item] == n:
                # The assumption here is that there is only one center for the star graph
                return item

        return None
    