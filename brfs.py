from collections import defaultdict

# BFS recursive function
def BFS(graph, queue, visited):
    if not queue:
        return
    node = queue.pop(0)
    if not visited[node]:
        visited[node] = True
        print(node, end=' ')
        for neighbor in graph[node]:
            queue.append(neighbor)
    BFS(graph, queue, visited)

# Initialize graph and input number of nodes
graph = defaultdict(list)
n = int(input("Enter number of nodes: "))

# Input values at nodes
for i in range(n):
    val = input(f"Enter value for node {i+1}: ")
    graph[i+1] = []

# Input edges between nodes
for i in range(n-1):
    u, v = map(int, input(f"Enter edge {i+1}: ").split())
    graph[u].append(v)
    graph[v].append(u)

# Perform BFS starting from node 1
visited = [False] * (n+1)
queue = [1]
BFS(graph, queue, visited)