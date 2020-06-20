#### creating adjacency matrix
adjMatrix = []
possible = open('possible.csv')
for line in possible:
	elements = line.split(',')
	for i in range(len(elements)):
		elements[i] = float(elements[i])
	adjMatrix.append(elements)

#### creating all distances matrix
alldist = []
allfile = open('alldist.csv')
for line in allfile:
	elements = line.split(',')
	for i in range(len(elements)):
		elements[i] = float(elements[i])
	alldist.append(elements)


### cities list
cities = ['Актопан', 'Иксмикильпан', 'Микскиауал', 'Атиталакия','Уэуэтока','Тисаюка','Экатепек','Мехико','Тескоко','Истапалука','Тлальманалько','Амекамека-де-Хуарес','Хонакатепек','Исукар-де-Матаморос','Сан-Хосе-Идальго']
print("All cities on our map: Актопан, Иксмикильпан, Микскиауал, Атиталакия, Уэуэтока,\nТисаюка, Экатепек, Мехико, Тескоко, Истапалука, Тлальманалько, Амекамека-де-Хуарес,\nХонакатепек, Исукар-де-Матаморос, Сан-Хосе-Идальго")
### creating neighbors dictionary
def FindNeighbors(adjMatrix):
	neighbors = {i:[] for i in range(len(adjMatrix))}
	for i in range(len(adjMatrix)):
		for j in range(len(adjMatrix[i])):
			if adjMatrix[i][j] > 0:
				neighbors[i].append(j)
	return neighbors

# finding neighbors
neighbors = FindNeighbors(adjMatrix)

# Processing start city
startCity = input("Type your START city: ")
for i in range(len(cities)):
	if cities[i] == startCity:
		startIndex = i

# Procesing last city
finishCity = input("Type your FINISH city: ")
for i in range(len(cities)):
	if cities[i] == finishCity:
		finishIndex = i



####### GREEDY ALGORITHM
# Initiating start values of route and it's length
route = [startCity]
routeLength = 0
currCity = startCity
currIndex = startIndex

## Performing Greedy shortest path finding algorithm
# It is heuristic so there's no guarantee of minimal result 

while currCity != finishCity:  # While we didn't reach our last city
	mindist = alldist[currIndex][finishIndex]    # Minimum distance by the right line
	minNeigh = currIndex
	for neigh in neighbors[currIndex]:   # Checking all neighbors of city
		if alldist[neigh][finishIndex] < mindist:  # If its distance is less than current minimum distance
			mindist = alldist[neigh][finishIndex]   #  changing minimum distance
			minNeigh = neigh                       # assigning closest neighbor
			currCity = cities[neigh]             # going to that city
	routeLength += adjMatrix[currIndex][minNeigh]    # Adding distance between cities
	currIndex = cities.index(currCity)     # assigning new index of current city
	route.append(currCity)      # Adding next city to route


# Showing results 
print(f"{startCity}->{finishCity}")
print("Route found by greedy algorithm:")

for city in route:
	if city != finishCity:
		print(f"{city}->", end='')
	else:
		print(city)

print(f"Route length is: {round(routeLength, 2)} km")

#### A STAR ALGORITHM
# Start and goal indices
start = startIndex + 1
goal = finishIndex + 1

# Initiating arrays for work comfort
result = []
closed = []  # Vertices that we have already seen
opened = []  # Vertices that we should see in future
cost = [-1] * len(alldist)    # Travel cost from start vertex to x
funcValue = [-1] * len(alldist)    # Heuristic function value
parent = [-1] * len(alldist)    # Setting default parents
minim = []

# Setting some start values
cost[start - 1] = 0
opened.append(start - 1)
funcValue[start] = (alldist[start - 1][goal - 1])

flag = False

while len(opened) != 0 and flag == False:
	for i in range(len(opened)):
		minim.append([funcValue[opened[i]], opened[i]])

	minM = minim[0][1]
	for i in range(1, len(minim)):
		if minim[i - 1][0] > minim[i][0]:
			minM = minim[i][1]

	current = minM     # Minimal distance between adjacent vertices
	if current == goal - 1:
		flag = True

	opened.remove(current)
	closed.append(current)

	for neigh in neighbors[current]:
		tentativeScore = cost[current] + alldist[current][neigh]

		if neigh in closed and tentativeScore >= cost[neigh]:
			continue

		if neigh not in closed or tentativeScore < cost[neigh]:
			parent[neigh] = current
			cost[neigh] = tentativeScore
			funcValue[neigh] = cost[neigh] + alldist[neigh][goal - 1]
			if neigh not in opened:
				opened.append(neigh)
			

for i in range(len(closed)):
	result.append(cities[closed[i]])

print(f"{startCity}->{finishCity}")
print("Route found with А* algorithm: ")

for city in result:
	if city != finishCity:
		print(f"{city}->", end='')
	else:
		print(city)
print(f"Route length: {round(routeLength, 2)} km")


