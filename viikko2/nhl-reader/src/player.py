class Player:
    def __init__(self, name, nationality, assists, goals, team, games, id):
        self.name = name
        self.nationality=nationality
        self.assists=assists
        self.goals=goals
        self.team=team
        self.games=games
        self.id=id

    
    def __str__(self):
        return f'{self.name:20} {self.team:15}  {self.goals} + {self.assists} = {self.goals+self.assists}'
