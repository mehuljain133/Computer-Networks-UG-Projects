#  Simulate and implement Dijkstra algorithm for shortest path routing. 

import heapq

class Dijkstra:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        # Initialize the adjacency matrix with some random weights
        self.graph = [[0 if i == j else float('inf') for j in range(num_nodes)] for i in range(num_nodes)]
        
    def add_edge(self, u, v, weight):
        # Add a directed edge from u to v with the given weight
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # If the graph is undirected

    def shortest_path(self, start):
        # Initialize the distances and visited set
        distances = [float('inf')] * self.num_nodes
        distances[start] = 0
        
        # Min-heap priority queue for the next node to process
        priority_queue = [(0, start)]  # (distance, node)
        
        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)
            
            # If the current distance is already greater than the recorded one, skip it
            if current_dist > distances[current_node]:
                continue
            
            # Process all the neighbors of the current node
            for neighbor in range(self.num_nodes):
                if self.graph[current_node][neighbor] != float('inf'):
                    distance = self.graph[current_node][neighbor]
                    new_dist = current_dist + distance
                    
                    # If a shorter path is found
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(priority_queue, (new_dist, neighbor))
        
        return distances

    def print_shortest_paths(self, start):
        distances = self.shortest_path(start)
        print(f"Shortest paths from node {start}:")
        for i in range(self.num_nodes):
            print(f"Node {i}: {distances[i]}")

# Example usage:
if __name__ == "__main__":
    num_nodes = 6
    dijkstra = Dijkstra(num_nodes)
    
    # Add edges (u, v, weight)
    dijkstra.add_edge(0, 1, 7)
    dijkstra.add_edge(0, 2, 9)
    dijkstra.add_edge(0, 5, 14)
    dijkstra.add_edge(1, 2, 10)
    dijkstra.add_edge(1, 3, 15)
    dijkstra.add_edge(2, 3, 11)
    dijkstra.add_edge(2, 5, 2)
    dijkstra.add_edge(3, 4, 6)
    dijkstra.add_edge(4, 5, 9)

    # Print the shortest paths from node 0
    dijkstra.print_shortest_paths(0)
