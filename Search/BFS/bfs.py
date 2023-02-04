'''
Breadth First Search (BFS)
Reference: https://favtutor.com/blogs/breadth-first-search-python
'''

'''
Graph represented as key-value pairs where each subnodes of a node
(whether empty or not) is represented as a list.

Example:
Given the graph, try to search for a set of numbers that results to a sum of 25.

Graph
                    0
    ---------------------------------
    |               |               |
    1               5               8
    |               |               |
---------       ----------          4
|       |       |        |
2       3       6        9
                |
                7

KV Graph = { 
    0 : [1,5,8], 
    1 : [2,3],
    5 : [6,9],
    8 : [4]
    2 : [],
    3 : [],
    6 : [7],
    7 : [],
    9 : []
    4 : []
}

Starting Node: 0
Target Sum Node: 25
'''
graph = {
  '0' : ['1','5','8'],
  '1' : ['2','3'],
  '5' : ['6','9'],
  '8' : ['4'],
  '2' : [],
  '3' : [],
  '6' : ['7'],
  '7' : [],
  '9' : [],
  '4' : []
}

def bfs(visited, graph, node, sum): #function for BFS
    visited.append(node)
    queue.append(node)
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
visited = [] # List for visited nodes.
queue = []     #Initialize a queue
print("Breadth-First Search")
bfs(visited, graph, '0')