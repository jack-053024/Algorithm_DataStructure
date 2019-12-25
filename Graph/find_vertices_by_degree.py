#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2019/12/24 13:56
# Author  : Jack
from graph import UndirectedGraph
from collections import deque

def find_vertices_by_degree(graph, from_vertex: int, degree: int) -> list:
    """
    Given a graph, starting vertex and degree, find vertices that are associated with that starting vertex,
    such as find_vertices_by_degree(graph, 1, 3), which means to find the third-degree friend relationship of
    vertex 1.
    :param graph: Given graph.
    :param from_vertex: Starting vertex.
    :param degree: Given degree.
    :return: A list that contains the third-degree friend relationship of vertex 1.
    """
    # 1. Process parameters
    if len(graph) <= 1:
        return []
    if degree == 1:
        return graph[from_vertex]
    # 2. Define auxiliary variables
    res = []
    queue = deque()
    visited = [False] * len(graph)
    # 3. Make breadth-first search according to degree
    # 3.1 Let from_vertex enqueued firstly, and set it to True.
    queue.append(from_vertex)
    visited[from_vertex] = True
    # 3.2 Start loop, and get one degree vertices for each cycle.
    while queue and degree > 0:
        queue_len = len(queue)  # Number of vertices in a layer.
        temp = []               # Temporary variable for storing vertices in a layer.
        for _ in range(queue_len):              # Traverse one layer each round.
            vertex = queue.popleft()
            for neighbour in graph[vertex]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    temp.append(neighbour)
                    visited[neighbour] = True   # If enqueued, it should be set to True.
        degree -= 1
        res.append(temp)
    # 4. return res
    return res


if __name__ == "__main__":
    graph = UndirectedGraph(8)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(3, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    print(graph)
    print(find_vertices_by_degree(graph, 0, 3))
