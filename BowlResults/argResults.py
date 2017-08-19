def argResults():
	finM = []
	numGames=[]
	for year in range (2002, 2017):
		yearInd = year - 2001
		yearStr = str(year)
		f = open("Co" + yearStr + ".csv", "r")
		yearRes = f.readlines()
		f.close()
		numGames.append(len(yearRes)-2)
		modelNames = yearRes[0].split(",")

		finalResults = yearRes[-1].split(",")

		print(len(finalResults))

		i = 1
		while i < len(finalResults) and finalResults[i] is not '0':
			modelName = modelNames[i]
			if modelName[-1] == "\n":
				modelName = modelName[:-1]
			numberScored = finalResults[i]
			j = 0
			modelFound = False
			while j < len(finM) and not modelFound: 
				if (finM[j][0] == modelName):
					finM[j][yearInd] = numberScored
					modelFound = True
				j = j + 1
			if not modelFound:
				finM.append([modelName, "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
				finM[j][yearInd] = numberScored
			i = i + 1

	i = 0
	while i < len(finM):
		numCorrect = 0
		numGamesForModel = 0.0
		for y in range( 1, 16):
			if finM[i][y] is not "":
				numCorrect = numCorrect + int(finM[i][y])
				numGamesForModel = numGamesForModel + numGames[y -1]
		finM[i].append(str(numCorrect/numGamesForModel))
		i = i + 1

	f = open("EndRes.csv", "w")
	f.write(",")
	f.write(",".join(str(e) for e in numGames))
	f.write("\n")
	for model in finM:
		f.write(",".join(model))
		f.write("\n")

	

if __name__ == '__main__':
    argResults()