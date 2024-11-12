import pandas as pd


def find_shortest_path(start_node, end_node, graph):
    all_nodes = pd.concat([graph['u'], graph['v']]).unique()
    distances = {node_id: float('inf') for node_id in all_nodes}
    previous_node = {node_id: None for node_id in all_nodes}

    distances[start_node] = 0
    visited_nodes = set()

    while end_node not in visited_nodes:
        current_node = min((node_id for node_id in set(distances) - visited_nodes), key=distances.get)
        visited_nodes.add(current_node)

        for _, row in graph.iterrows():
            if current_node in (row['u'], row['v']):
                neighbor = row['v'] if row['u'] == current_node else row['u']
                new_distance = distances[current_node] + row['length']

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_node[neighbor] = current_node

    path = []
    current_node = end_node

    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_node[current_node]

    return path
