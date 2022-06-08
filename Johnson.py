# Implementation of Johnson's algorithm in Python3
import time
# Import function to initialize the dictionary
from collections import defaultdict
MAX_INT = float('Inf')

# Returns the vertex with minimum
# distance from the source
def minDistance(dist, visited):

	(minimum, minVertex) = (MAX_INT, 0)
	for vertex in range(len(dist)):
		if minimum > dist[vertex] and visited[vertex] == False:
			(minimum, minVertex) = (dist[vertex], vertex)

	return minVertex


# Dijkstra Algorithm for Modified
# Graph (removing negative weights)
def Dijkstra(graph, modifiedGraph, src):

	# Number of vertices in the graph
	num_vertices = len(graph)

	# Dictionary to check if given vertex is
	# already included in the shortest path tree
	sptSet = defaultdict(lambda : False)

	# Shortest distance of all vertices from the source
	dist = [MAX_INT] * num_vertices

	dist[src] = 0

	for count in range(num_vertices):

		# The current vertex which is at min Distance
		# from the source and not yet included in the
		# shortest path tree
		curVertex = minDistance(dist, sptSet)
		sptSet[curVertex] = True

		for vertex in range(num_vertices):
			if ((sptSet[vertex] == False) and
				(dist[vertex] > (dist[curVertex] +
				modifiedGraph[curVertex][vertex])) and
				(graph[curVertex][vertex] != 0)):
				
				dist[vertex] = (dist[curVertex] +
								modifiedGraph[curVertex][vertex]);

	# Print the Shortest distance from the source
	for vertex in range(num_vertices):
		print ('Vertex ' + str(vertex) + ': ' + str(dist[vertex]))

# Function to calculate shortest distances from source
# to all other vertices using Bellman-Ford algorithm
def BellmanFord(edges, graph, num_vertices):

	# Add a source s and calculate its min
	# distance from every other node
	dist = [MAX_INT] * (num_vertices + 1)
	dist[num_vertices] = 0

	for i in range(num_vertices):
		edges.append([num_vertices, i, 0])

	for i in range(num_vertices):
		for (src, des, weight) in edges:
			if((dist[src] != MAX_INT) and
					(dist[src] + weight < dist[des])):
				dist[des] = dist[src] + weight

	# Don't send the value for the source added
	return dist[0:num_vertices]

# Function to implement Johnson Algorithm
def JohnsonAlgorithm(graph):

	edges = []

	# Create a list of edges for Bellman-Ford Algorithm
	for i in range(len(graph)):
		for j in range(len(graph[i])):

			if graph[i][j] != 0:
				edges.append([i, j, graph[i][j]])

	# Weights used to modify the original weights
	modifyWeights = BellmanFord(edges, graph, len(graph))

	modifiedGraph = [[0 for x in range(len(graph))] for y in
					range(len(graph))]

	# Modify the weights to get rid of negative weights
	for i in range(len(graph)):
		for j in range(len(graph[i])):

			if graph[i][j] != 0:
				modifiedGraph[i][j] = (graph[i][j] +
						modifyWeights[i] - modifyWeights[j]);

	print ('Modified Graph: ' + str(modifiedGraph))

	# Run Dijkstra for every vertex as source one by one
	for src in range(len(graph)):
		print ('\nShortest Distance with vertex ' +
						str(src) + ' as the source:\n')
		Dijkstra(graph, modifiedGraph, src)

# Driver Code
# graph = [[0, -5, 2, 3],
# 		[0, 0, 4, 0],
# 		[0, 0, 0, 1],
# 		[0, 0, 0, 0]]

		    # 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
graph =    [[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    2,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #0
	        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    7,  2,  0,  0,  0,  0,  0,  0,  0,  0,   16,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #1
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #2
            [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  3,    0,  0,  0,  3,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #3
            [ 0,  0,  0,  0,  0,  0,  1,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #4
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  7,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #5
            [ 0,  0,  0,  0,  1,  0,  0,  1,  0,  0,    0,  0,  0,  0,  0,  1,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #6
            [ 0,  0,  0,  0,  0,  0,  1,  0,  0,  0,    0,  0,  0,  5,  1,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #7
            [ 0,  0,  0,  1,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #8
			[ 0,  0,  1,  3,  0,  0,  0,  0,  0,  0,    3,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #9
			
			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
	        [ 2,  7,  0,  0,  0,  0,  0,  0,  0,  3,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #10
			[ 0,  2,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #11
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,   11,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #12
			[ 0,  0,  0,  3,  0,  0,  0,  5,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0, 10,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #13
			[ 0,  0,  0,  0,  0,  0,  0,  1,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #14
			[ 0,  0,  0,  0,  0,  0,  1,  0,  0,  0,    0,  0,  0,  0,  0,  0,  1,  1,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #15
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  1,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #16
			[ 0,  0,  0,  0,  0,  7,  0,  0,  0,  0,    0,  0,  0,  0,  0,  1,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0, 11,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #17
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0, 20,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #18
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  1,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #19

			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
	        [ 0, 16,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0, 11,  0,  0,  0,  0,  0,  0,  0,    0,  5,  0,  0,  7,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #20
  			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  1,    5,  0,  0,  1,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #21 
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0, 10,  0,  0,  0,  0, 20,  0,    0,  0,  0,  0,  0,  0, 11,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #22
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  1,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #23
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    7,  0,  0,  0,  0,  0,  0,  0,  7,  0,    2,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #24
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  9,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #25
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0, 11,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #26
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  9,  0,  0,  5,  0,    0,  0,  0,  0,  0,  0,  0,  7,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #27
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  7,  0,  0,  5,  0,  1,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #28
            [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  1,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #29
			
			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
	        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  2,  0,  0,  0,  0,  0,    0,  6,  0,  0,  0,  0,  0,  0,  3,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #30
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    6,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #31 
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  6,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #32
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  8,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #33
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0, 11,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #34
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  8,  0,  0,  8,  0,  0,  0,     0,  0,  0,  3,  0,  0,  0,  0,  0,  0,     0,  0,  0], #35
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  6,  0,  0,  8,  0,  0,  0,  0,     0,  0,  0,  0,  6,  0,  0,  0,  0,  0,     0,  0,  0], #36
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  7,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  9,  5,  0,  0,  0,  0,     0,  0,  0], #37
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    3,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  6,     0,  0, 20], #38
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     3,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #39

			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
	        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  3,     0, 12,  0,  0,  0,  0,  0,  6,  0,  0,     0,  0,  0], #40
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    12,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #41
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0, 10,  0,  0,  0,     0,  0,  0], #42 
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0, 	3,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #43
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0, 	6, 	9,  0,  0,     0,  0,  0,  0,  0,  0,  5,  0,  0,  0,     0,  0,  0], #44
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0, 	5,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0], #45
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0, 10,  0,  5,  0,  0,  0,  0,  0,     0,  7,  0], #46
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     6,  0,  0,  0,  0,  0,  0,  0,  0,  5,     5,  0,  0], #47
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  2,     0,  0,  0], #48
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  6,  0,     0,  0,  0,  0,  0,  0,  0,  5,  2,  0,     0,  0,  0], #49

			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
	        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  0,  5,  0,  0,     0,  0,  0], #50
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0,  0,  0,  0,  7,  0,  0,  0,     0,  0,  0], #51
			[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    0,  0,  0,  0,  0,  0,  0,  0, 20,  0,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,     0,  0,  0]  #52
		]

start = time.time()
JohnsonAlgorithm(graph)
end = time.time()
print(f"Runtime of the program is {end - start}")

