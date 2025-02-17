def overlap_graph(patterns):
    graph = {}

    for pattern1 in patterns:
        suffix = pattern1[1:]  # Correct suffix (last k-1 chars)
        for pattern2 in patterns:
            if pattern1 != pattern2 and pattern2.startswith(suffix):
                if pattern1 not in graph:
                    graph[pattern1] = []
                graph[pattern1].append(pattern2)

    return graph

def print_graph(graph):
    for node, neighbors in sorted(graph.items()):  # Sorting ensures consistency
        if neighbors:  # Only print nodes with edges
            print(f"{node}: {' '.join(neighbors)}")

# Read and process the file
with open("dataset_30182_10.txt", "r", encoding="utf-8") as file:
    seqs = file.read().strip()  # Remove trailing spaces and newlines
patterns = seqs.split()

# Compute and print the overlap graph
graph = overlap_graph(patterns)
print_graph(graph)
