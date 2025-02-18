def read_input_from_file(filename):
    """Reads k from a file."""
    with open(filename, "r") as f:
        k = int(f.readline().strip())  # Read k from the first line
    return k

def de_bruijn(k):
    """Generate a k-universal circular binary string using an iterative DFS."""
    # Generate all (k-1)-bit nodes
    nodes = {format(i, f'0{k-1}b') for i in range(2**(k-1))}  # Set for uniqueness
    graph = {node: [node[1:] + "0", node[1:] + "1"] for node in nodes}

    # Iterative DFS (Hierholzer’s Algorithm)
    start_node = "0" * (k-1)
    stack = [start_node]
    path = []

    while stack:
        node = stack[-1]
        if graph[node]:
            stack.append(graph[node].pop())
        else:
            path.append(stack.pop())

    # Convert Eulerian path to circular string
    return "".join(node[0] for node in path) + start_node


k = 9
print(de_bruijn(9))