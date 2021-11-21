# https://cses.fi/problemset/task/1682
# run file with command: 
# python3 flights_check.py < flights_check.txt

from collections import defaultdict
import sys

'''
Check if all nodes are connected to node 1, check for both 
going to and coming back.
Runtime Error... Solution may need to use Disjoint Sets
'''
class Solution:
    def flights_check(self, num_cities, flights):
        adj_list = defaultdict(list)
        adj_list2 = defaultdict(list)
        for a, b in flights:
            adj_list[a].append(b)
            adj_list2[b].append(a)

        self.num_cities = num_cities
        self.adj_list = adj_list
        
        visited = set()
        self.dfs(1, visited, adj_list)
        for i in range(2, num_cities+1):
            if i not in visited:
                print("NO")
                print(f"1 {i}")
        
        visited2 = set()
        self.dfs(1, visited2, adj_list2)
        for i in range(2, num_cities+1):
            if i not in visited2:
                print("NO")
                print(f"{i} 1")
                return

        print("YES")
        return
    
    def dfs(self, node, visited, adj_list):

        visited.add(node)
        
        for neighbours in adj_list[node]:
            if neighbours not in visited:
                self.dfs(neighbours, visited, adj_list)
        
        return

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    num_cities, num_flights = list(map(int, input().split(" ")))
    flights = []
    for _ in range(num_flights):
        flight = list(map(int, input().split(" ")))
        flights.append(flight)

    Solution().flights_check(num_cities, flights)
