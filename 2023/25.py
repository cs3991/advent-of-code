import itertools
from typing import List, Set

from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter

with open("ex25.txt") as file:
    ex = [line for line in file]

with open("input25.txt") as file:
    inp = [line for line in file]
inp = ex
# print(inp)
tic()
# -------- Part 1 -----------
print('   PART 1')
graph = defaultdict(set)
for l in inp:
    node_a, connected_nodes_str = l.strip().split(': ')
    connected_nodes = []
    for node_b in connected_nodes_str.split(' '):
        connected_nodes.append(node_b)
        graph[node_a].add(node_b)
        graph[node_b].add(node_a)


def find_paths(graph: dict[str, set[str]], start_node: str, end_node: str) -> list[list[str]]:
    queue: list[list[str]] = [[start_node]]
    next_queue: list[list[str]] = []
    visited: set[str] = set()
    result: list[list[str]] = []
    while len(queue) != 0:
        path: list[str]
        for path in queue:
            for node in graph[path[-1]]:
                if node not in path and node not in visited:
                    if node == end_node:
                        result.append(path + [node])
                    else:
                        next_queue.append(path + [node])
                        visited.add(node)
        queue = next_queue.copy()
        next_queue = []
    return result

for node_a, node_b in itertools.combinations(graph.keys(), 2):
    print(node_a, node_b)
    paths = find_paths(
        graph=graph,
        start_node=node_a,
        end_node=node_b,
    )

    for path in paths:
        print(path)

    common_nodes = set(paths[0][1:-1])

    for path in paths:
        node_to_remove = set()
        for node in common_nodes:
            if node not in path:
                node_to_remove.add(node)
        common_nodes = common_nodes.difference(node_to_remove)

    print(common_nodes)

toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')

toc('Part 2 done in')
