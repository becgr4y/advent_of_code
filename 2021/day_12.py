with open("2021/inputs/12") as f:
    data = [line.strip().split("-") for line in f]

all_nodes = sorted(list(set([inner for outer in data for inner in outer])))

graph = {node: set() for node in all_nodes}

for row in data:
    graph[row[0]].add(row[1])
    graph[row[1]].add(row[0])

# Part 1
paths = [["start"]]
valid_paths = []

while paths:
    current_path = paths.pop()
    current_vertex = current_path[-1]

    if current_vertex == "end":
        valid_paths.append(current_path)
        continue

    for connected_vertex in graph[current_vertex]:
        if connected_vertex.isupper() | (connected_vertex not in current_path):
            paths.append(current_path + [connected_vertex])

print(len(valid_paths))

# Part 2
paths = [["start"]]
valid_paths = []

while paths:
    current_path = paths.pop()
    current_vertex = current_path[-1]

    if current_vertex == "end":
        valid_paths.append(current_path)
        continue

    for connected_vertex in graph[current_vertex]:
        lower = [vertex for vertex in current_path if vertex.islower()]
        single_lower = len(lower) == len(set(lower))
        if (
            connected_vertex.isupper()
            | (connected_vertex not in current_path)
            | (single_lower & (connected_vertex != "start"))
        ):
            paths.append(current_path + [connected_vertex])

print(len(valid_paths))
