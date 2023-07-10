class Match:
    homeTeamName, awayTeamName = None, None
    homeTeamScore, awayTeamScore = 0, 0
    def __init__(self, homeTeamName, awayTeamName):
        self.homeTeamName, self.awayTeamName = homeTeamName, awayTeamName

    def updateScore(self, homeTeamScore, awayTeamScore):
        self.homeTeamScore, self.awayTeamScore = homeTeamScore, awayTeamScore

    def getAllGoals(self):
        return self.homeTeamScore + self.awayTeamScore