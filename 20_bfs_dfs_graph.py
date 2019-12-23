#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2019/12/21 22:08
# Author  : Jack
from typing import IO, List, Optional
from collections import deque

class Graph(object):
    """Undirected graph."""
    def __init__(self, vertex_num: int):
        self._vertex_num = vertex_num   # The number of vertices.
        # From scratch. The adjacency list.
        self._adj_list = [[] for _ in range(vertex_num)]

    def add_edge(self, s: int, t: int) -> bool:
        """
        Making a connection between two vertices.
        :param s: vertex s.
        :param t: vertex t.
        :return: True or False
        """
        if s > self._vertex_num or t > self._vertex_num:
            return False
        self._adj_list[s].append(t)
        self._adj_list[t].append(s)
        return True

    def __str__(self):
        return str(self._adj_list)

    def _generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> IO[str]:
        """
        Generate path from vertex s to vertex t using prev array.
        :param s: vertex s
        :param t: vertex t
        :param prev: Previous vertex of a certain vertex.
        :return: Path.
        """
        if prev[t] and s != t:
            self._generate_path(s, prev[t], prev)
        print(t, end="->")

    def bfs(self, s: int, t: int) -> None:
        """
        Print the shortest path from vertex s to vertex t using breadth first search.
        :param s: Vertex s
        :param t: Vertex t
        :return: IO string
        """
        if s == t: return
        visited = [False] * self._vertex_num
        queue = deque()
        queue.append(s)
        prev = [None] * self._vertex_num

        while queue:
            vertex = queue.popleft()
            for neighbour in self._adj_list[vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = vertex
                    if neighbour == t:
                        self._generate_path(s, t, prev)
                        return
                    visited[neighbour] = True
                    queue.append(neighbour)

    def dfs(self, s: int, t: int) -> None:
        """
        Print the path from vertex s to vertex t using depth first search. (Not shortest)
        :param s: Vertex s
        :param t: Vertex t
        :return: IO string
        """
        found = False
        prev = [None] * self._vertex_num
        visited = [False] * self._vertex_num

        def _dfs(from_vertex):
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neightbour in self._adj_list[from_vertex]:
                if not visited[neightbour]:
                    prev[neightbour] = from_vertex
                    _dfs(neightbour)

        _dfs(s)
        self._generate_path(s, t, prev)


if __name__ == "__main__":
    graph = Graph(8)
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
    graph.bfs(0, 7)
    print()
    graph.dfs(0, 7)





