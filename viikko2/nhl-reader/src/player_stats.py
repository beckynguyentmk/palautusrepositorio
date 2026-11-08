# pylint: disable=too-few-public-methods

class PlayerStats:
    def __init__(self,reader):
        self.players=reader.get_players()

    def top_scorers_by_nationality(self,nationality):
        players_list=[]
        for player in self.players:
            if player.nationality==nationality:
                players_list.append(player)

        players_list.sort(key=lambda player: player.goals+player.assists, reverse=True)

        return players_list

    def top_scorers_by_team(self, team):
        players_list=[]
        for player in self.players:
            if player.team==team:
                players_list.append(player)

        players_list.sort(key=lambda player: player.goals+player.assists, reverse=True)

        return players_list

    def top_goal_scorers(self, how_many):
        players_list=[]
        for player in self.players:
            players_list.append(player)

        players_list.sort(key=lambda player: player.goals, reverse=True)

        return players_list[:how_many]
