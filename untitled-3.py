# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13S-KG7NsnKc0PydzjbhztLMtgwEzsSBG

##домашнее задание
"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def transpose(self):
        transposed_graph = Graph(self.vertices)
        for i in self.graph:
            for j in self.graph[i]:
                transposed_graph.add_edge(j, i)
        return transposed_graph

    def kosaraju_algorithm(self):
        visited = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

        transposed_graph = self.transpose()

        visited = [False] * self.vertices
        strongly_connected_components = []

        while stack:
            current_vertex = stack.pop()
            if not visited[current_vertex]:
                current_scc = []
                transposed_graph.dfs(current_vertex, visited, current_scc)
                strongly_connected_components.append(current_scc)

        return strongly_connected_components

# Пример использования:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

scc = g.kosaraju_algorithm()
print("Компоненты сильной связности:", scc)