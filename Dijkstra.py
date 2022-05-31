from collections import defaultdict

class Node_Distance :

    def __init__(self, name : int, dist : int) :
        self.name = name
        self.dist = dist

class Graph :

    def __init__ (self, node_count : int) :
        # Store the adjacency list as a dictionary
        # The default dictionary would create an empty list as a default (value) 
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.node_count = node_count

    def Add_Into_Adjlist (self, src : int, node_dist : Node_Distance(int,int)) :
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path (self, source : int) :

        # Initialize the distance of all the nodes from the source node to infinity
        distance = [999999999999] * self.node_count
        # Distance of source node to itself is 0
        distance[source] = 0

        # Create a dictionary of { node, distance_from_source }
        dict_node_length = {source: 0}

        while dict_node_length :

            # Get the key for the smallest value in the dictionary
            # i.e Get the node with the shortest distance from the source
            current_source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
            del dict_node_length[current_source_node]

            for node_dist in self.adjlist[current_source_node] :
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist

                # Edge relaxation
                if distance[adjnode] > distance[current_source_node] + length_to_adjnode :
                    distance[adjnode] = distance[current_source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        for i in range(self.node_count) :
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))

def main() :

	g = Graph(53)

    # Node 1: 
	g.Add_Into_Adjlist(1, Node_Distance(11, 2))

    # Node 2:
	g.Add_Into_Adjlist(2, Node_Distance(11, 7))
	g.Add_Into_Adjlist(2, Node_Distance(12, 2))
	g.Add_Into_Adjlist(2, Node_Distance(21, 16))

    # Node 3:
	g.Add_Into_Adjlist(3, Node_Distance(10, 1))

    # Node 4:
	g.Add_Into_Adjlist(4, Node_Distance(9, 1))
	g.Add_Into_Adjlist(4, Node_Distance(10, 3))
	g.Add_Into_Adjlist(4, Node_Distance(14, 3))

    # Node 5: 
	g.Add_Into_Adjlist(5, Node_Distance(7, 1))

	# Node 6: 
	g.Add_Into_Adjlist(6, Node_Distance(18, 7))

	# Node 7:
	g.Add_Into_Adjlist(7, Node_Distance(5, 1))
	g.Add_Into_Adjlist(7, Node_Distance(8, 1))
	g.Add_Into_Adjlist(7, Node_Distance(16, 1))

	# Node 8:
	g.Add_Into_Adjlist(8, Node_Distance(7, 1))
	g.Add_Into_Adjlist(8, Node_Distance(15, 1))

	# Node 9:
	g.Add_Into_Adjlist(9, Node_Distance(4, 1))

	# Node 10:
	g.Add_Into_Adjlist(10, Node_Distance(4, 3))
	g.Add_Into_Adjlist(10, Node_Distance(3, 1))
	g.Add_Into_Adjlist(10, Node_Distance(11, 3))

	# Node 11:
	g.Add_Into_Adjlist(11, Node_Distance(1, 2))
	g.Add_Into_Adjlist(11, Node_Distance(2, 7))
	g.Add_Into_Adjlist(11, Node_Distance(10, 3))

	# Node 12:
	g.Add_Into_Adjlist(12, Node_Distance(2, 2))

	# Node 13:
	g.Add_Into_Adjlist(13, Node_Distance(21, 11))

	# Node 14:
	g.Add_Into_Adjlist(14, Node_Distance(4, 3))
	g.Add_Into_Adjlist(14, Node_Distance(8, 5))
	g.Add_Into_Adjlist(14, Node_Distance(23, 10))

	# Node 15:
	g.Add_Into_Adjlist(15, Node_Distance(8, 1))

	# Node 16:
	g.Add_Into_Adjlist(16, Node_Distance(7, 1))
	g.Add_Into_Adjlist(16, Node_Distance(17, 1))
	g.Add_Into_Adjlist(16, Node_Distance(18, 1))

	# Node 17:
	g.Add_Into_Adjlist(17, Node_Distance(16, 1))

	# Node 18:
	g.Add_Into_Adjlist(18, Node_Distance(6, 7))
	g.Add_Into_Adjlist(18, Node_Distance(16, 1))
	g.Add_Into_Adjlist(18, Node_Distance(35, 11))

	# Node 19:
	g.Add_Into_Adjlist(19, Node_Distance(23, 20))

	# Node 20:
	g.Add_Into_Adjlist(20, Node_Distance(22, 1))

	# Node 21:
	g.Add_Into_Adjlist(21, Node_Distance(2, 16))
	g.Add_Into_Adjlist(21, Node_Distance(13, 11))
	g.Add_Into_Adjlist(21, Node_Distance(22, 5))
	g.Add_Into_Adjlist(21, Node_Distance(25, 7))
	
	# Node 22:
	g.Add_Into_Adjlist(22, Node_Distance(24, 1))
	g.Add_Into_Adjlist(22, Node_Distance(20, 1))
	g.Add_Into_Adjlist(22, Node_Distance(21, 5))
	
	
	# Node 23:
	g.Add_Into_Adjlist(23, Node_Distance(14, 10))
	g.Add_Into_Adjlist(23, Node_Distance(19, 20))
	g.Add_Into_Adjlist(23, Node_Distance(27, 11))

	# Node 24:
	g.Add_Into_Adjlist(24, Node_Distance(22, 1))
	
	# Node 25:
	g.Add_Into_Adjlist(25, Node_Distance(31, 2))
	g.Add_Into_Adjlist(25, Node_Distance(29, 7))
	g.Add_Into_Adjlist(25, Node_Distance(21, 7))
	
	# Node 26:
	g.Add_Into_Adjlist(26, Node_Distance(28, 9))
	
	# Node 27:
	g.Add_Into_Adjlist(27, Node_Distance(23, 11))
	
	# Node 28:
	g.Add_Into_Adjlist(28, Node_Distance(26, 9))
	g.Add_Into_Adjlist(28, Node_Distance(38, 7))
	g.Add_Into_Adjlist(28, Node_Distance(29, 5))
	
	# Node 29:
	g.Add_Into_Adjlist(29, Node_Distance(30, 1))
	g.Add_Into_Adjlist(29, Node_Distance(25, 7))
	g.Add_Into_Adjlist(29, Node_Distance(28, 5))
	
	# Node 30:
	g.Add_Into_Adjlist(30, Node_Distance(29, 1))
	
	# Node 31:
	g.Add_Into_Adjlist(31, Node_Distance(25, 2))
	g.Add_Into_Adjlist(31, Node_Distance(32, 6))
	g.Add_Into_Adjlist(31, Node_Distance(39, 3))
	
	# Node 32:
	g.Add_Into_Adjlist(32, Node_Distance(31, 6))
	
	# Node 33:
	g.Add_Into_Adjlist(33, Node_Distance(37, 6))
	
	# Node 34:
	g.Add_Into_Adjlist(34, Node_Distance(36, 8))
	
	# Node 35:
	g.Add_Into_Adjlist(35, Node_Distance(18, 11))
	
	# Node 36:
	g.Add_Into_Adjlist(36, Node_Distance(34, 8))
	g.Add_Into_Adjlist(36, Node_Distance(37, 8))
	g.Add_Into_Adjlist(36, Node_Distance(44, 3))

	# Node 37:
	g.Add_Into_Adjlist(37, Node_Distance(33, 6))
	g.Add_Into_Adjlist(37, Node_Distance(36, 8))
	g.Add_Into_Adjlist(37, Node_Distance(45, 6))	

	# Node 38:
	g.Add_Into_Adjlist(38, Node_Distance(28, 7))
	g.Add_Into_Adjlist(38, Node_Distance(45, 9))
	g.Add_Into_Adjlist(38, Node_Distance(46, 5))

	# Node 39:
	g.Add_Into_Adjlist(39, Node_Distance(31, 3))
	g.Add_Into_Adjlist(39, Node_Distance(50, 6))
	g.Add_Into_Adjlist(39, Node_Distance(53, 20))

	# Node 40:
	g.Add_Into_Adjlist(40, Node_Distance(41, 3))

	# Node 41:
	g.Add_Into_Adjlist(41, Node_Distance(40, 3))
	g.Add_Into_Adjlist(41, Node_Distance(42, 12))
	g.Add_Into_Adjlist(41, Node_Distance(48, 6))

	# Node 42:
	g.Add_Into_Adjlist(42, Node_Distance(41, 12))

	# Node 43:
	g.Add_Into_Adjlist(43, Node_Distance(47, 10))

	# Node 44:
	g.Add_Into_Adjlist(44, Node_Distance(47, 10))

	# Node 45:
	g.Add_Into_Adjlist(45, Node_Distance(37, 6))
	g.Add_Into_Adjlist(45, Node_Distance(38, 9))
	g.Add_Into_Adjlist(45, Node_Distance(47, 5))

	# Node 46:
	g.Add_Into_Adjlist(46, Node_Distance(38, 5))

	# Node 47:
	g.Add_Into_Adjlist(47, Node_Distance(43, 10))
	g.Add_Into_Adjlist(47, Node_Distance(45, 5))
	g.Add_Into_Adjlist(47, Node_Distance(52, 7))

	# Node 48:
	g.Add_Into_Adjlist(48, Node_Distance(41, 6))
	g.Add_Into_Adjlist(48, Node_Distance(50, 5))
	g.Add_Into_Adjlist(48, Node_Distance(51, 5))

	# Node 49:
	g.Add_Into_Adjlist(49, Node_Distance(50, 2))

	# Node 50:
	g.Add_Into_Adjlist(50, Node_Distance(39, 6))
	g.Add_Into_Adjlist(50, Node_Distance(48, 5))
	g.Add_Into_Adjlist(50, Node_Distance(49, 2))

	# Node 51:
	g.Add_Into_Adjlist(51, Node_Distance(48, 5))

	# Node 52:
	g.Add_Into_Adjlist(52, Node_Distance(47, 7))

	# Node 53:
	g.Add_Into_Adjlist(52, Node_Distance(39, 20))

	g.Dijkstras_Shortest_Path(0)
	print("\n")
	g.Dijkstras_Shortest_Path(5);


if __name__ == "__main__" :
	main()
