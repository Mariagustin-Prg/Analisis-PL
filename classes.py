class Jugador:
    def __init__(self, name, surname, position, age, nation, team, old_team=None) -> None:
        self.name = name
        self.surname= surname
        self.position = position
        self.age = age
        self.nation = nation
        self.team = team
        self.old_team = old_team

    def __stats__(self, matches, goals, assists, minutes, passes) -> None:
        self.matches = matches
        self.goals = goals
        self.assists = assists
        self.minutes = minutes
        self.passes = passes
        


class Equipo:
    
    def __init__(self, name) -> None:
        self.name = name
        
    def __stats__(self, points:int , wins:int , draws:int, losses:int, goals_f:int, goals_c:int) -> None:
        self.points = points
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_f = goals_f
        self.goals_c = goals_c
        self.diff = goals_f - goals_c
    
    def getStats(self) -> list:
        return [self.points, self.wins, self.draws, self.losses,
                self.goals_f, self.goals_c, self.diff]