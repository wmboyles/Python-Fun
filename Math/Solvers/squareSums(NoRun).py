from math import sqrt

#Number of edges any node n has in the Square-Sum problem where the max is m
def squareSum(n,m):
    count=0
    for i in range(1,int(sqrt(2*m))+1): #i^2, aka a, will be the number we're ading to
        a = i**2
        if(n<a and n<=m and a!=2*n and a-n<m):
            #print("%i + %i = %i"%(n,a-n,a)) #optional print
            count+=1
    return count


# Same as above, but these are put into a txt file.
# For example, "6, 10" b/c 6+10=16 which is a square
# Best for use through below function

def squareSumCSV(n,m):
    NetworkFile = open("SquareSumNet.csv",'a')
    for i in range(1,int(sqrt(2*m))+1): #i^2, aka a, will be the number we're ading to
        a = i**2
        if(n<a and n<=m and a!=2*n and a-n<m): NetworkFile.write("%i, %i\n"%(n,a-n))
    NetworkFile.close()

def networkCSV(m): #Generates a CSV file corresponding to the network for the Square-Sum problem
    for i in range(1,m+1): squareSumCSV(i,m)

'''
The below function finds a path between two nodes if it exists.
The data structure looks like this:
{'A': ['B', 'C'],
 'B': ['C', 'D'],
 'C': ['D'],
 'D': ['C'],
 'E': ['F'],
 'F': ['C']}

where 'A' is connected to 'B' and 'C', and 'C' is connected to 'D'.
In this structure connections are directional.
'''
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

    
