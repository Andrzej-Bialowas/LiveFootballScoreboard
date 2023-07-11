from Match import Match

class Scoreboard:
    matchList = []

    def __init__(self):
        self.matchList = []

    def startMatch(self, homeTeamName, awayTeamName):
        """
        This function starts a new match after checking if any of the teams is not playing already.
        :param homeTeamName:  Name of the home team
        :param awayTeamName:  Name of the away team
        """
        if not self.__isTeamAlreadyPlaying(homeTeamName, awayTeamName):
            newMatch = Match(homeTeamName, awayTeamName)
            self.matchList.append(newMatch)

    def updateMatch(self, homeTeamName, awayTeamName, homeTeamScore, awayTeamScore):
        '''
        This function updates an existing match with a result specified in the argument
        :param homeTeamName: Name of the home team
        :param awayTeamName: Name of the away team
        :param homeTeamScore: Score for the home team to be updated with
        :param awayTeamScore: Score for the away team to be updated with
        :return: returns True if successful
        '''
        match = self.__findMatch(homeTeamName, awayTeamName)
        if not match:
            raise Exception("Missing match")

        if not self.__isScoreValid(homeTeamScore) or not self.__isScoreValid(awayTeamScore):
            raise ValueError("Wrong score")

        match.updateScore(homeTeamScore, awayTeamScore)
        return True

    def __findMatch(self, homeTeamName, awayTeamName):
        '''
        Private method used in other methods for checking for an existing match
        :param homeTeamName: Name of the home team
        :param awayTeamName: Name of the away team
        :return: returns a match object if the specified match was found
        '''
        for match in self.matchList:
            if match.homeTeamName == homeTeamName and match.awayTeamName == awayTeamName:
                return match

    def __isScoreValid(self, score):
        '''
        Private method for checking if the score is of type int and it's value of 0 or greater
        :param score: Score for a single team
        :return: returns true if input type is int and score is 0 or greater
        '''
        return isinstance(score, int) and score >= 0

    def __isTeamAlreadyPlaying(self, homeTeamName, awayTeamName):
        '''
        Private method for checking if any of the specified two teams is already playing in another match.
        :param homeTeamName: Name of the home team
        :param awayTeamName: Name of the away team
        :return: returns False is none of the two teams is already playing
        '''
        for match in self.matchList:
            if match.homeTeamName in [homeTeamName, awayTeamName] or match.awayTeamName in [homeTeamName, awayTeamName]:  # make a function for checking if any of the team exists
                raise Exception("One of these teams is already playing.")
        return False

    def finishMatch(self, homeTeamName, awayTeamName):
        '''
        Finishes the match by removing it from the scoreboard
        :param homeTeamName: Name of the home team
        :param awayTeamName: Name of the away team
        :return: returns True if the match was successfully found and removed
        '''
        match = self.__findMatch(homeTeamName, awayTeamName)
        if match:
            self.matchList.remove(match)
            return True

    def getSummary(self):
        '''
        A simple method for getting the whole scoreboard summary with the team names and scores, sorted from highest score and starting time.
        :return: returns a list with formatted strings for each of the matches currently happening
        '''
        if self.matchList:
            sortedList = sorted(self.matchList, key=lambda m: (m.getAllGoals(), self.matchList.index(m)), reverse=True)
            formattedSortedList = []
            for match in sortedList:
                formattedSortedList.append(f"{match.homeTeamName} {match.homeTeamScore} - {match.awayTeamName} {match.awayTeamScore}")
            return formattedSortedList
