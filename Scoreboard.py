from Match import Match

class Scoreboard:
    matchList = []

    def __init__(self):
        self.matchList = []

    def startMatch(self, homeTeamName, awayTeamName):
        if not self.__isTeamAlreadyPlaying(homeTeamName, awayTeamName):
            newMatch = Match(homeTeamName, awayTeamName)
            self.matchList.append(newMatch)

    def updateMatch(self, homeTeamName, awayTeamName, homeTeamScore, awayTeamScore):
        match = self.__findMatch(homeTeamName, awayTeamName)
        if not match:
            raise Exception("Missing match")

        if not self.__isScoreValid(homeTeamScore) or not self.__isScoreValid(awayTeamScore):
            raise ValueError("Wrong score")

        match.updateScore(homeTeamScore, awayTeamScore)

    def __findMatch(self, homeTeamName, awayTeamName):
        for match in self.matchList:
            if match.homeTeamName == homeTeamName and match.awayTeamName == awayTeamName:
                return match

    def __isScoreValid(self, score):
        return isinstance(score, int) and score >= 0

    def __isTeamAlreadyPlaying(self, homeTeamName, awayTeamName):
        for match in self.matchList:
            if match.homeTeamName in [homeTeamName, awayTeamName] or match.awayTeamName in [homeTeamName, awayTeamName]:  # make a function for checking if any of the team exists
                raise Exception("One of these teams is already playing.")
        return False

    def finishMatch(self, homeTeamName, awayTeamName):
        match = self.__findMatch(homeTeamName, awayTeamName)
        if match:
            self.matchList.remove(match)

    def getSummary(self):
        if self.matchList:
            sortedList = sorted(self.matchList, key=lambda m: (m.getAllGoals(), self.matchList.index(m)), reverse=True)
            formattedSortedList = []
            for match in sortedList:
                formattedSortedList.append(f"{match.homeTeamName} {match.homeTeamScore} - {match.awayTeamName} {match.awayTeamScore}")
            return formattedSortedList

