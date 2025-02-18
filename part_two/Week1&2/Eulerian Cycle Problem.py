from collections import defaultdict
import random

def read_graph_from_file(filename):
    graph = defaultdict(list)
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(": ")
            node = int(parts[0])
            edges = list(map(int, parts[1].split()))
            graph[node] = edges
    return graph

def find_eulerian_cycle(graph):
    adj_list = defaultdict(list)
    for node, edges in graph.items():
        adj_list[node] = edges[:]

    cycle = []
    stack = []
    start_node = random.choice(list(graph.keys()))
    stack.append(start_node)

    while stack:
        node = stack[-1]
        if adj_list[node]:
            next_node = adj_list[node].pop()
            stack.append(next_node)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]

filename = "dataset_30187_2.txt"
graph = read_graph_from_file(filename)
result = find_eulerian_cycle(graph)
print("Eulerian Cycle:", " ".join(map(str, result)))
