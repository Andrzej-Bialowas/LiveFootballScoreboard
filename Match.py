class Match:
    homeTeamName, awayTeamName = None, None
    homeTeamScore, awayTeamScore = 0, 0
    def __init__(self, homeTeamName, awayTeamName):
        self.homeTeamName, self.awayTeamName = homeTeamName.title(), awayTeamName.title()

    def updateScore(self, homeTeamScore, awayTeamScore):
        '''
        Updates the score of a Match object specified as a parameter
        :param homeTeamScore: Result of the home team to update with
        :param awayTeamScore: Result of the away team to update with
        :return:
        '''
        self.homeTeamScore, self.awayTeamScore = homeTeamScore, awayTeamScore

    def getAllGoals(self):
        '''
        Summarizes the goal score for a single match by adding two single scores
        :return: returns the summarized goal value
        '''
        return self.homeTeamScore + self.awayTeamScore