from player_reader import PlayerReader

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