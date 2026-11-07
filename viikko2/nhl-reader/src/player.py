# pylint: disable=too-few-public-methods
# pylint: disable=too-many-positional-arguments
class Player:
    def __init__(self, name, nationality, assists, goals, team, games, id_num):
        self.name = name
        self.nationality=nationality
        self.assists=assists
        self.goals=goals
        self.team=team
        self.games=games
        self.id=id_num



    def __str__(self):
        return (f'{self.name:20} {self.team:15}'
                f'{self.goals} + {self.assists} = {self.goals+self.assists}')
