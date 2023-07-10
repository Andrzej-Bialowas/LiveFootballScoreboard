from Match import Match

class Scoreboard:
    matchList = []

    def __init__(self):
        self.matchList = []

    def startMatch(self, homeTeamName, awayTeamName):
        for match in self.matchList:
            if match.homeTeamName in [homeTeamName, awayTeamName] or match.awayTeamName in [homeTeamName, awayTeamName]:  # make a function for checking if any of the team exists
                raise Exception("One of these teams is already playing.")
        newMatch = Match(homeTeamName, awayTeamName)
        self.matchList.append(newMatch)

    def updateMatch(self, homeTeamName, awayTeamName, homeTeamScore, awayTeamScore):
        match = self.__findMatch(homeTeamName, awayTeamName)
        if not match:
            raise Exception("Missing match")

        if not self.__isScoreValid(homeTeamScore) or not self.__isScoreValid(awayTeamScore):
            raise ValueError("Wrong score")

        self.updateScore(homeTeamScore, awayTeamScore)

    def __findMatch(self, homeTeamName, awayTeamName):
        for match in self.matchList:
            if match.homeTeamName == homeTeamName and match.awayTeamName == awayTeamName:
                return match

    def __isScoreValid(self, score):
        return isinstance(score, int) and score >= 0
