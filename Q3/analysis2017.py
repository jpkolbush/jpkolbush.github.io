import scipy.stats as stats

scores = [[89.4,76.1,134,64.1,50,100.3,64.2,80,85.2,69.7,72,104.2],
		[111.1,89.2,86.2,77.4,98.8,78.4,89.6,86.1,108.5,98.5,78.7,79.9],
		[76.4,69.4,65.8,95.5,124,68.9,118.5,65.8,95.1,130.9,61.8,91.7],
		[68.8,116,91.6,65.8,89.8,69,69.1,89.7,80.2,107.9,62.4,108.8],
		[67.9,81.4,84,54.8,93.3,114.4,101.3,89.9,117,87.8,76.8,71.2],
		[75.4,56.8,90.2,53.1,123.6,101.1,85,64.4,97.6,93,92.4,81.2],
		[41,79,93.8,82.7,112.9,79.6,99.6,139.2,59.5,70.8,60.1,97.4],
		[83.5,69.2,63,88.6,103.8,121.5,79.6,86.8,136.3,89.8,52.4,80.3],
		[56,71.5,76.9,107.5,100.5,57.5,94.5,100.8,78.1,65.1,82.4,105.8],
		[81.9,89.7,91.7,112.6,81.2,81,101.7,62.8,64.4,84.5,126.9,86.7],
		[89.7,97.8,57.7,162.4,67.6,130,132.5,82,102.8,74.5,85.1,52.8],
		[105.5,81.3,54.7,88.4,162.6,88.2,81.3,122,105.5,83,108,109.2]]

i = 0
j = 0
#for each player, find out how his week 1 average 
CURRENTWEEK = 0
weeklyAverages = []
results =[]
while CURRENTWEEK < 11:
	#find the league average
	weeklyTotal = 0
	for score in scores[CURRENTWEEK]:
		weeklyTotal+= score
	weeklyAverages.append(weeklyTotal/12.0)

	weeklyTotal = 0
	for week in weeklyAverages:
		weeklyTotal+=week
	weeklyAverage = weeklyTotal/float(len(weeklyAverages))

	#print(weeklyAverage)

	#find the players average through the CURRENTWEEK and the average of the remaining weeks
	#[currAvg, remAvg] to be appended to playerAverages
	playerAverages = []
	currentPlayer = 0
	for currentPlayer in range(12):
		priorTotal = 0
		afterTotal = 0 
		for week in range(11):
			if week <= CURRENTWEEK:
				priorTotal += scores[week][currentPlayer]
			else:
				afterTotal += scores[week][currentPlayer]

		playerAverages.append([priorTotal/(CURRENTWEEK + 1.0), afterTotal/(11.0 - CURRENTWEEK)])

	#print(playerAverages)

	pAvg = 0

	std = 20.77989
	for player in range(12):
		A = stats.norm(weeklyAverage, std).pdf(playerAverages[player][1])
		#print('prob in total average model is' + str(A))
		B = stats.norm(playerAverages[player][0], std).pdf(playerAverages[player][1])
		#print('prob in user model is' + str(B))
		pAvg += B/(A + B)
		# perc = (playerAverages[player][1] - weeklyAverage)/()

	print(pAvg/12.0)
	results.append(pAvg/12)
	CURRENTWEEK += 1

finalAvg = 0
for i in range(1, 11):
	finalAvg += results[i]
print(finalAvg/10.0)
