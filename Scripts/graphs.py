class Vertex (object):

    def __init__(self, label):
        self.label = label
        self.visited = False

    def __str__(self):
        return str(self.label)

class Graph(object):   
    def __init__(self):
        self.vertices = []
        self.adjMat = []

    # old implementation from school - link in readme makes more sense
