from collections import defaultdict, Counter


def read_graph_from_file(filename):
    graph = defaultdict(list)
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(": ")
            node = int(parts[0])
            edges = list(map(int, parts[1].split()))
            graph[node] = edges
    return graph


def find_eulerian_path(graph):
    in_degree = Counter()
    out_degree = Counter()

    for node, edges in graph.items():
        out_degree[node] += len(edges)
        for dest in edges:
            in_degree[dest] += 1

    start_node = None
    end_node = None

    for node in set(in_degree.keys()).union(out_degree.keys()):
        diff = out_degree[node] - in_degree[node]
        if diff == 1:
            start_node = node
        elif diff == -1:
            end_node = node

    if start_node is None:
        start_node = next(iter(graph))

    adj_list = defaultdict(list, {node: edges[:] for node, edges in graph.items()})

    path = []
    stack = [start_node]

    while stack:
        node = stack[-1]
        if adj_list[node]:
            stack.append(adj_list[node].pop())
        else:
            path.append(stack.pop())

    return path[::-1]


filename = ""
graph = read_graph_from_file(filename)
result = find_eulerian_path(graph)
print("Eulerian Path:", " ".join(map(str, result)))
