'''
Breadth First Search (BFS)
Reference: https://favtutor.com/blogs/breadth-first-search-python
'''

'''
Graph represented as key-value pairs where each subnodes of a node
(whether empty or not) is represented as a list.

Example:
            4
    -----------------
    |               |
    1               5
---------       ---------
|       |       |
2       3       6
                |
                7

Graph = { 
    4 : [1,5], 
    1 : [2,3],
    5 : [6],
    2 : [],
    3 : [],
    6 : [7],
    7 : []
    }

Starting Node: 4
Traversal: 4 > 1 > 5 > 2 > 3 > 6 > 7
'''
graph = {
  '4' : ['1','5'],
  '1' : ['2','3'],
  '5' : ['6'],
  '2' : [],
  '3' : [],
  '6' : ['7'],
  '7' : [],
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '4')    # function calling