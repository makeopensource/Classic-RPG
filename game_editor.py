from array import *
from crpg import generate
from crpg import Game

#Altered for purpose from : https://www.codecademy.com/learn/learn-data-structures-and-algorithms-with-python/modules/nodes/cheatsheet
class gameMap:
    def __init__(self, value, type, name, pathType, previous_node=None):
        self.value = value
        self.type = type
        self.name = name
        self.pathType = pathType
        self.previous_node = previous_node
        self.next_node = set()
        
    def set_next_node(self, next_node):
        self.next_node.add(next_node)

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node

    def get_next_node(self):
        return self.next_node

    def get_previous_node(self):
        return self.previous_node

    def get_value(self):
        return self.value

    def get_pathType(self):
        return self.pathType

    def get_name(self):
        return self.name

    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level


def find(array , val):
    for pos in range(len(array)):
        if(array[pos][0] == val):
            return pos
    return -1


def addNode(array, parent, target, pType, newVal):
    branch = findNode(parent, target)
    nodeAddHelp(array, branch, pType, newVal)

def nodeAddHelp(array, parent, pType, newVal):
    pos = find(ar ,newVal )
    newNode = gameMap(newVal,array[pos][1],array[pos][2], pType)
    newNode.set_previous_node(parent)
    parent.set_next_node(newNode)

def findNode(parent, target):
    next = parent.get_value()
    if(next == target):
        return parent
    if (next == None ):
        return None
    q = []  # Create a queue
    for val in parent.get_next_node():
        q.append(val); # Enqueue root
    while (len(q) != 0):
        n = len(q)
        # If this node has children
        while (n > 0):
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0)
            if( p.get_value() == target):
                return p
            # Enqueue all children of the dequeued item
            for i in p.get_next_node():
                q.append(i)
            n -= 1# Print new line between two levels


def printMap(parent):
    if (parent == None or parent.get_next_node() == set()):
        return
    # Standard level order traversal code
    # using queue
    q = []  # Create a queue
    for val in parent.get_next_node():
        q.append(val); # Enqueue root
    while (len(q) != 0):
     
        n = len(q)
        out= ""
  
        # If this node has children
        while (n > 0):
         
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0)
            out += p.get_name()+" | "
   
            # Enqueue all children of the dequeued item
            for i in p.get_next_node():
                q.append(i)
            n -= 1
        print(out)
        print() # Print new line between two levels


def printFileDir(root):
    if (root == None or root.get_next_node() == set()):
        return
    else:
         printFileDirHelp(0, root)


def printFileDirHelp(depth, root):
    point = "\033["+str(91+depth)+"m {}\033[00m" .format("o")
    if (not(root == None or root.get_next_node() == set())):
        print((isRoot(depth)*'|')+((depth)*' ')+point+root.get_name())
        for node in root.get_next_node():
            printFileDirHelp(depth+1,node)
    else:
        print((isRoot(depth)*'|')+(depth*' ')+point+root.get_name())

def isRoot(num):
    if(num>0):
        return 1
    return 0


with open("game_libary/game-2-layout.dl",'r') as f:
    nodes = []
    contents = f.read()
    nodes, connections = contents.split("\n---\n", maxsplit=1)
    node = (nodes.split('\n'))
    ar = [["" for i in range(4)] for o in range(len(node))]

    for pos in range(len(ar)):
        #May need to change depending of file format
        values=node[pos].split(" | ")
        for val in range(len(values)):
            ar[pos][val]=values[val]

    basePos = find(ar , '1')
    base = gameMap('1', ar[basePos][1], ar[basePos][2], None)

    connection = connections.split('\n')
    if(connection[-1] ==""):
        connection.pop()

    for con in connection:
        commands = con.split()
        addNode(ar ,base , commands[0],commands[1],commands[2])
        
    #printMap(base)

    printFileDir(base)

