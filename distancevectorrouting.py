# Simulate and implement distance vector routing algorithm

import random

class DistanceVectorRouting:
    def __init__(self, num_routers, max_distance=10):
        self.num_routers = num_routers
        self.max_distance = max_distance
        
        # Create an adjacency matrix (initializing with random distances)
        self.adj_matrix = [[random.randint(1, max_distance) if i != j else 0 for j in range(num_routers)] for i in range(num_routers)]
        self.routing_tables = [{} for _ in range(num_routers)]
        
    def initialize_routing_tables(self):
        # Each router initializes its table with its neighbors' distance
        for i in range(self.num_routers):
            for j in range(self.num_routers):
                if self.adj_matrix[i][j] != 0:
                    self.routing_tables[i][j] = self.adj_matrix[i][j]
                else:
                    self.routing_tables[i][j] = float('inf')  # unreachable destination initially

    def update_routing_table(self, router_id):
        # Update routing table of router `router_id` based on distance vectors from neighbors
        updated = False
        for i in range(self.num_routers):
            if i != router_id:
                # Compare current route with the route through the neighboring router
                new_distance = self.adj_matrix[router_id][i]
                for j in range(self.num_routers):
                    if self.adj_matrix[router_id][j] != float('inf'):
                        distance_via_j = self.routing_tables[j].get(i, float('inf'))
                        total_distance = new_distance + distance_via_j
                        if total_distance < self.routing_tables[router_id].get(i, float('inf')):
                            self.routing_tables[router_id][i] = total_distance
                            updated = True
        return updated
    
    def exchange_routing_tables(self):
        # Simulate the exchange of routing tables among all routers
        updated_any_router = False
        for router_id in range(self.num_routers):
            updated = self.update_routing_table(router_id)
            if updated:
                updated_any_router = True
        return updated_any_router
    
    def simulate(self, iterations=10):
        # Run the distance vector algorithm until the tables converge
        print(f"Initial Adjacency Matrix: {self.adj_matrix}")
        self.initialize_routing_tables()
        print(f"Initial Routing Tables: {self.routing_tables}")
        
        for _ in range(iterations):
            updated = self.exchange_routing_tables()
            if not updated:
                print(f"Convergence reached at iteration {_}")
                break
            print(f"Routing Tables after iteration {_}: {self.routing_tables}")
        
        print(f"Final Routing Tables: {self.routing_tables}")

# Example usage
if __name__ == "__main__":
    # Create a network with 5 routers
    num_routers = 5
    max_distance = 10
    routing_protocol = DistanceVectorRouting(num_routers, max_distance)

    # Run the Distance Vector Routing simulation
    routing_protocol.simulate()
