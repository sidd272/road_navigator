class Node:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adj_List = []

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getVisited(self):
        return self.visited

    def setVisited(self, visited):
        self.visited = visited

    def get_adjList(self):
        return self.adj_List

    def set_adjList(self, adjList):
        self.adjList = adjList


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Node(i) for i in range(num_vertices)]

    def addNode(self, label):
        new_Node = Node(label)
        self.vertices.append(new_Node)
        self.num_vertices = self.num_vertices+1

    def removeNode(self, label):
        for i in range(self.num_vertices):
            if self.vertices[i].getLabel == label:
                del self.vertices[i]
                self.num_vertices = self.num_vertices-1
                return

    def addEdge(self, start_label, end_label):
        start_node = None
        end_node = None  # to check whether the 2 starting and ending vertices exist in the graph,if they exist edge is added
        for vertex in self.vertices:
            if vertex.getLabel == start_label:
                start_node = vertex
            if vertex.getLabel == end_label:
                end_node = vertex
        if start_node is not None and end_node is not None:
            start_node.adj_List.append(end_node)
            end_node.adj_List.append(start_node)

    def delEdge(self, start_label, end_label):
        start_node = None
        end_node = None  # to check whether the vertices are present in the graph
        for vertex in self.vertices:
            if vertex.getLabel == start_label:
                start_node = vertex
            if vertex.getLabel == end_label:
                end_node = vertex
        if start_node is not None and end_node is not None:
            start_node.adj_List.remove(end_node)
            end_node.adj_List.remove(start_node)

    def Print(self):
        for vertex in self.vertices:
            print(vertex.label, end=":")

            for node in vertex.get_adjList:
                print(node.label, end=" ")
            print()

    def BFS(self, start_label):
        start_vertex = None
        bfs = []

        for vertex in self.vertices:
            if vertex.label == start_label:
                start_vertex = vertex
        if start_vertex is None:
            return bfs
        queue = [start_vertex]
        start_vertex.setVisited(True)
        while len(queue) != 0:
            node = queue.pop(0)
            bfs.append(node)
            for adj in node.adj_List:
                if adj.
