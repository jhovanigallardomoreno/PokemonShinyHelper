class Pokemon:
    def __init__(self, name, start, game):
        self.name = name
        self.dateStart = start
        self.dateCaught = "In progress..."
        self.encounterNum = 0
        self.probability = 1/4096
        self.game = game
    def __str__(self):
        if self.dateCaught == "In progress...":
            return "You are currently searching for %s, since %s in Pokemon %s. You have encountered this pokemon %d times,\
 there is a %f probability that you should have found a shiny  on your next encounter." % (self.name, self.dateStart, self.game, self.encounterNum, self.probability)
        else:
            return "On %s, you caught a shiny %s on Pokemon %s. Your hunt started on %s, it took you %d encounters,\
 and the probability that you caught in those number of encounters is %f" % (self.dateCaught, self.name, self.game, self.dateStart, self.encounterNum, self.probability)
    #Setter Functions
    def setDate(self, date):
        self.dateCaught = date
    def setEncounter(self, num):
        self.encounterNum = num
    def setProbability(self, prob):
        self.probability = prob
    #Getter functions
    def getName(self):
        return self.name
    def getDateStart(self):
        return self.dateStart
    def getDateEnd(self):
        return self.dateCaught
    def getEncounter(self):
        return self.encounterNum
    def getProbability(self):
        return self.probability
    def getGame(self):
        return self.game
    def optionCreate(self, i):
        if self.dateCaught == "In progress...":
            print("(%d) : %s : Started on %s : %s : %d : %s" % (i, self.name, self.dateStart, self.dateCaught, self.encounterNum, self.game))
        else:
            print("(%d) : %s : Started on %s : Caught on %s : %d : %s" % (i, self.name, self.dateStart, self.dateCaught, self.encounterNum, self.game))