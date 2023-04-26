from collections import defaultdict


def DFS(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(neighbor, graph, visited)


def eulerian_path(graph):
    # Check if graph has an eulerian path
    odd_count = 0
    for node in graph:
        if len(graph[node]) % 2 != 0:
            odd_count += 1
        if odd_count > 2:
            return "Ейлерівський шлях не існує"

    # Find start node
    start = next(iter(graph))
    for node in graph:
        if len(graph[node]) % 2 != 0:
            start = node
            break

    # Find eulerian path
    path = []
    stack = [start]
    while stack:
        current_node = stack[-1]
        if graph[current_node]:
            next_node = graph[current_node].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())

    return path[::-1]


# Define graph
graph = defaultdict(list)
data = [
    [0, 22, 98, 0, 0, 0, 0, 81],
    [22, 0, 0, 62, 87, 0, 0, 99],
    [98, 0, 0, 0, 0, 81, 82, 70],
    [0, 62, 0, 0, 99, 0, 97, 70],
    [0, 87, 0, 99, 0, 0, 13, 0],
    [0, 0, 81, 0, 0, 0, 9, 59],
    [0, 0, 82, 97, 13, 9, 0, 80],
    [81, 99, 70, 70, 0, 59, 80, 0]
]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != 0:
            graph[i].append(j)

# Find eulerian path
path = eulerian_path(graph)
print(path)
