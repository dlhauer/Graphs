"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        visited = {starting_vertex}
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            u = queue.dequeue()
            print(u)
            for v in self.get_neighbors(u):
                if v not in visited:
                    queue.enqueue(v)
                    visited.add(v)
                
    def dft(self, starting_vertex):
        visited = {starting_vertex}
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            u = stack.pop()
            print(u)
            for v in self.get_neighbors(u):
                if v not in visited:
                    stack.push(v)
                    visited.add(v)

    def dft_recursive(self, starting_vertex):
        visited = {starting_vertex}

        def dft_print(starting_vertex):
            print(starting_vertex)
            for v in self.get_neighbors(starting_vertex):
                if v not in visited:
                    visited.add(v)
                    dft_print(v)

        dft_print(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        parent_map = {starting_vertex: None}
        visited = {starting_vertex}
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            u = queue.dequeue()
            if u == destination_vertex:
                break
            for v in self.get_neighbors(u):
                if v not in visited:
                    parent_map[v] = u
                    queue.enqueue(v)
                    visited.add(v)
            
        return self.get_path(destination_vertex, parent_map)

    def dfs(self, starting_vertex, destination_vertex):
        parent_map = {starting_vertex: None}
        visited = {starting_vertex}
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            u = stack.pop()
            if u == destination_vertex:
                break
            for v in self.get_neighbors(u):
                if v not in visited:
                    parent_map[v] = u
                    stack.push(v)
                    visited.add(v)
        
        return self.get_path(destination_vertex, parent_map)
        
        
    def get_path(self, destination_vertex, parent_map):
        path = [destination_vertex]
        parent = parent_map[destination_vertex]
        while parent:
            path.insert(0, parent)
            parent = parent_map[parent]
        return path

    def dfs_recursive(self, starting_vertex, destination_vertex):
        visited = {starting_vertex}
        path = []

        def search(starting_vertex, destination_vertex):
            if starting_vertex == destination_vertex:
                path.insert(0, starting_vertex)
                return True
            for v in self.get_neighbors(starting_vertex):
                if v not in visited:
                    visited.add(v)
                    if search(v, destination_vertex):
                        path.insert(0, starting_vertex)
                        return True
        
        search(starting_vertex, destination_vertex)
        return path

    def dfs_recursive_two(self, starting_vertex, destination_vertex):
            visited = {starting_vertex}
            path = [starting_vertex]

            def search(path, destination_vertex):
                if path[-1] == destination_vertex:
                    # path.insert(0, starting_vertex)
                    return path
                for v in self.get_neighbors(path[-1]):
                    if v not in visited:
                        visited.add(v)
                        path_copy = path.copy()
                        path_copy.append(v)
                        return search(path_copy, destination_vertex)
            
            return search(path, destination_vertex)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
    print(graph.dfs_recursive_two(1, 6))
