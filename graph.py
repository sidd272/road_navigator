class Node:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adj_List = [self]

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
            if self.vertices[i].getLabel() == label:
                del self.vertices[i]
                self.num_vertices = self.num_vertices-1
                return

    def addEdge(self, start_label, end_label):
        start_node = None
        end_node = None  # to check whether the 2 starting and ending vertices exist in the graph,if they exist edge is added
        for vertex in self.vertices:
            if vertex.getLabel() == start_label:
                start_node = vertex
            if vertex.getLabel() == end_label:
                end_node = vertex
        if start_node is not None and end_node is not None:
            start_node.adj_List.append(end_node)
            end_node.adj_List.append(start_node)

    def delEdge(self, start_label, end_label):
        start_node = None
        end_node = None  # to check whether the vertices are present in the graph
        for vertex in self.vertices:
            if vertex.getLabel() == start_label:
                start_node = vertex
            if vertex.getLabel() == end_label:
                end_node = vertex
        if start_node is not None and end_node is not None:
            start_node.adj_List.remove(end_node)
            end_node.adj_List.remove(start_node)

    def Print(self):
        for vertex in self.vertices:
            print(vertex.label, end=":")

            for node in vertex.get_adjList():
                print(node.getLabel(), end=" ")
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
                if adj.getVisited() == False:
                    queue.append(adj)
                    adj.setVisited(True)
        for it in self.vertices:
            it.setVisited(False)
        return bfs
    def DFS(self,start_label):
        start_vertex=None
        dfs=[]
        for vertices in self.vertices:
            if vertices.label==start_label:
                start_vertex=vertices
        if start_vertex is None:
            return dfs
        stack=[start_vertex]
        start_vertex.setVisited(True)    
        while(stack):
            vertex=stack.pop()
            dfs.append(vertex)
            for vertices in vertex.get_adjList():
                if vertices.getVisited()==False:
                    stack.append(vertices)
                    vertices.setVisited(True)
        for it in self.vertices:
            it.setVisited(False)
        return dfs


def main():
    a = Graph(3)
    a.addNode(1)
    a.addNode(2)
    a.addNode(3)
    a.addNode(5)
    a.addNode(7)
    a.addEdge(1, 2)
    a.addEdge(2, 3)
    a.addEdge(5, 7)
    a.addEdge(3, 5)
    bfs = a.BFS(1)
    for it in bfs:
        print(it.getLabel())
    dfs=a.DFS(1)
    for it in dfs:
        print(it.getLabel())

if __name__ == "__main__":
    main()
