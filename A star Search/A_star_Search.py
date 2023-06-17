class Node:
    def __init__(self, nodeName , parent, g, h):
        self.nodeName = nodeName
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g +h
        
adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    'D': [('C', 4)],
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0,
}

priority_queue = []

startNode = Node('S', None, 0, H['S'] )

priority_queue.append(startNode)

while priority_queue:
    priority_queue.sort(key = lambda x: x.f)
    currentNode = priority_queue.pop(0)
        
    if currentNode.nodeName == 'D':
        break
    
    childs = adjacency_list[currentNode.nodeName]
    
    for child in childs:
        childName , edge = child
        g = currentNode.g + edge
        h = H[childName]
        f = g + h 
        newNode = Node(childName, currentNode, g, h)
        priority_queue.append(newNode)
    currentNode = None
    
path = []
cost = currentNode.g 

while currentNode.parent is not None:
    path.insert(0, currentNode.nodeName)
    currentNode = currentNode.parent
    
path.insert(0, 'S')
print("Path: ", '->'.join(path))
print("cost: ", cost)