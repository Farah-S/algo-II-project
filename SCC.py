from collections import defaultdict
import time  
#This class represents a directed graph using adjacency list representation
class Graph:
    
        def __init__(self,vertices):
            self.V= vertices #No. of vertices
            self.graph = defaultdict(list) # default dictionary to store graph
    
        # function to add an edge to graph
        def addEdge(self,u,v):
            self.graph[u].append(v)
    
        # A function used by DFS
        def DFSUtil(self,v,visited):
            # Mark the current node as visited and print it
            visited[v]= True
            print (v)
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[v]:
                if visited[i]==False:
                    self.DFSUtil(i,visited)
    
    
        def fillOrder(self,v,visited, stack):
            # Mark the current node as visited 
            visited[v]= True
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[v]:
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
            stack = stack.append(v)
        
    
        # Function that returns reverse (or transpose) of this graph
        def getTranspose(self):
            g = Graph(self.V)
    
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph:
                for j in self.graph[i]:
                    g.addEdge(j,i)
            return g
    
    
    
        # The main function that finds and prints all strongly
        # connected components
        def printSCCs(self):
            
            stack = []
            # Mark all the vertices as not visited (For first DFS)
            visited =[False]*(self.V)
            # Fill vertices in stack according to their finishing
            # times
            for i in range(self.V):
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
    
            # Create a reversed graph
            gr = self.getTranspose()
            
            # Mark all the vertices as not visited (For second DFS)
            visited =[False]*(self.V)
    
            # Now process all vertices in order defined by Stack
            while stack:
                i = stack.pop()
                if visited[i]==False:
                    gr.DFSUtil(i, visited)
                    print("")
    
    # Create a graph given in the above diagram
# g = Graph(8)
# g.addEdge(0, 1)
# g.addEdge(1, 2)
# g.addEdge(2, 3)
# g.addEdge(3, 0)
# g.addEdge(2, 4)
# g.addEdge(4, 5)
# g.addEdge(5, 6)
# g.addEdge(6, 4)
# g.addEdge(6, 7)


g= Graph(53)

    # Node 1: 
g.addEdge(0, 10)

    # Node 2:
g.addEdge(1, 10)
g.addEdge(1, 11)
g.addEdge(1, 20)

    # Node 3:
g.addEdge(2, 9)

    # Node 4:
g.addEdge(3, 8)
g.addEdge(3, 9)
g.addEdge(3, 13)

    # Node 5: 
g.addEdge(4, 6)

	# Node 6: 
g.addEdge(5, 17)

	# Node 7:
g.addEdge(6, 4)
g.addEdge(6, 7)
g.addEdge(6, 15)

	# Node 8:
g.addEdge(7, 6)
g.addEdge(7, 14)
g.addEdge(7, 13)

	# Node 9:
g.addEdge(8, 3)

	# Node 10:
g.addEdge(9, 3)
g.addEdge(9, 2)
g.addEdge(9, 10)

	# Node 11:
g.addEdge(10, 0)
g.addEdge(10, 1)
g.addEdge(10, 9)

	# Node 12:
g.addEdge(11, 1)

	# Node 13:
g.addEdge(12, 20)

	# Node 14:
g.addEdge(13, 3)
g.addEdge(13, 7)
g.addEdge(13, 22)

	# Node 15:
g.addEdge(14, 7)

	# Node 16:
g.addEdge(15, 6)
g.addEdge(15, 16)
g.addEdge(15, 17)

	# Node 17:
g.addEdge(16, 15)

	# Node 18:
g.addEdge(17, 5)
g.addEdge(17, 15)
g.addEdge(17, 34)

	# Node 19:
g.addEdge(18, 22)

	# Node 20:
g.addEdge(19, 21)

	# Node 21:
g.addEdge(20, 1)
g.addEdge(20, 12)
g.addEdge(20, 21)
g.addEdge(20, 24)
	
	# Node 22:
g.addEdge(21, 23)
g.addEdge(21, 19)
g.addEdge(22, 20)
	
	
	# Node 23:
g.addEdge(22, 13)
g.addEdge(22, 18)
g.addEdge(22, 26)

	# Node 24:
g.addEdge(23, 21)
	
	# Node 25:
g.addEdge(24, 30)
g.addEdge(24, 28)
g.addEdge(24, 20)
	
	# Node 26:
g.addEdge(25, 27)
	
	# Node 27:
g.addEdge(26, 22)
	
	# Node 28:
g.addEdge(27, 25)
g.addEdge(27, 37)
g.addEdge(27, 28)
	
	# Node 29:
g.addEdge(28, 29)
g.addEdge(28, 24)
g.addEdge(28, 27)
	
	# Node 30:
g.addEdge(29, 28)
	
	# Node 31:
g.addEdge(30, 24)
g.addEdge(30, 31)
g.addEdge(30, 38)
	
	# Node 32:
g.addEdge(31, 30)
	
	# Node 33:
g.addEdge(32, 36)
	
	# Node 34:
g.addEdge(33, 35)
	
	# Node 35:
g.addEdge(34, 17)
	
	# Node 36:
g.addEdge(35, 33)
g.addEdge(35, 36)
g.addEdge(35, 43)

	# Node 37:
g.addEdge(36, 32)
g.addEdge(36, 35)
g.addEdge(36, 44)	

	# Node 38:
g.addEdge(37, 27)
g.addEdge(37, 44)
g.addEdge(37, 45)

	# Node 39:
g.addEdge(38, 30)
g.addEdge(38, 49)
g.addEdge(38, 52)

	# Node 40:
g.addEdge(39, 40)

	# Node 41:
g.addEdge(40, 39)
g.addEdge(40, 41)
g.addEdge(40, 47)

	# Node 42:
g.addEdge(41, 40)

	# Node 43:
g.addEdge(42, 46)

	# Node 44:
g.addEdge(43, 35)

	# Node 45:
g.addEdge(44, 36)
g.addEdge(44, 37)
g.addEdge(44, 46)

	# Node 46:
g.addEdge(45, 37)

	# Node 47:
g.addEdge(46, 42)
g.addEdge(46, 44)
g.addEdge(46, 51)

	# Node 48:
g.addEdge(47, 40)
g.addEdge(47, 49)
g.addEdge(47, 50)

	# Node 49:
g.addEdge(48, 49)

	# Node 50:
g.addEdge(49, 38)
g.addEdge(49, 47)
g.addEdge(49, 48)

	# Node 51:
g.addEdge(50, 47)

	# Node 52:
g.addEdge(51, 46)

	# Node 53:
g.addEdge(52, 38)
    
    
print ("Following are strongly connected components " +
                            "in given graph")

start = time.time()
g.printSCCs()
end = time.time()
print(f"Runtime of the program is {end - start}")                           


    #This code is contributed by Neelam Yadav
