from collections import defaultdict, deque

def read_input_from_file(filename):
    """Reads k and k-mers from a file."""
    with open(filename, "r") as f:
        lines = f.readlines()
        k = int(lines[0].strip())  # Read k from the first line
        kmers = [line.strip() for line in lines[1:]]  # Read the k-mers
    return k, kmers

def de_bruijn_graph(kmers):
    """Constructs the de Bruijn graph from k-mers."""
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def find_eulerian_path(graph):
    """Finds an Eulerian path in the de Bruijn graph using Hierholzer's algorithm."""
    in_degrees = defaultdict(int)
    out_degrees = defaultdict(int)

    # Compute in-degrees and out-degrees
    for node in graph:
        out_degrees[node] = len(graph[node])
        for neighbor in graph[node]:
            in_degrees[neighbor] += 1

    # Find start and end nodes
    start_node, end_node = None, None
    for node in set(in_degrees) | set(out_degrees):
        in_deg = in_degrees[node]
        out_deg = out_degrees[node]
        if out_deg - in_deg == 1:
            start_node = node
        elif in_deg - out_deg == 1:
            end_node = node

    if start_node is None:
        start_node = next(iter(graph))  # Choose any node if balanced

    # Hierholzer's algorithm for Eulerian path
    stack = [start_node]
    path = deque()

    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            path.appendleft(stack.pop())

    return list(path)

def path_to_genome(path):
    """Constructs a genome sequence from an Eulerian path."""
    genome = path[0]
    for node in path[1:]:
        genome += node[-1]
    return genome

def string_reconstruction(filename):
    """Solves the String Reconstruction Problem."""
    k, kmers = read_input_from_file(filename)
    graph = de_bruijn_graph(kmers)
    path = find_eulerian_path(graph)
    return path_to_genome(path)

# Example usage:
input_file = "dataset_30187_7 (1).txt"  # Your input file containing k and k-mers
reconstructed_string = string_reconstruction(input_file)
print(reconstructed_string)  # Prints the fully reconstructed genome
