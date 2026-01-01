"""
This scripts contains a unique class to build a "Team" structure
"""

class Team:
    def __init__(self) -> None:
        self.__initStats__()

    def __initStats__(self) -> None:
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

    def setStats(self, wins: int, losses: int, draws: int,
                    goals_for: int, goals_against: int, points: int) -> None:
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.points = points

    def getStats(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
            "goals_for": self.goals_for,
            "goals_against": self.goals_against,
            "points": self.points
        }
    
    def setProps(self, name: str, coach: str) -> None:
        self.__name__ = name
        self.coach = coach


    def getProps(self) -> dict:
        return {
            "name": self.__name__,
            "coach": self.coach,
        }