from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from player_reader import PlayerReader
from player_stats import PlayerStats

def ask_season():
    return Prompt.ask("[bold magenta]Season[/bold magenta]",
                      choices=[
                        "2018-19", "2019-20", "2020-21", "2021-22",
                        "2022-23", "2023-24", "2024-25", "2025-26"
                    ], default='2024-25')

def ask_nationality():
    return Prompt.ask("[bold magenta]Nationality[/bold magenta]",
                           choices=['USA','FIN','CAN','SWE',
                                    'CZE','RUS','SLO','FRA',
                                    'GBR','SVK','DEN','NED',
                                    'AUT','BLR','GER','SUI',
                                    'NOR','UZB','LAT','AUS'
                                    ])

def create_table(season,nationality):
    table=Table(title=f'Season {season} players from {nationality}')

    table.add_column('Released',style='cyan')
    table.add_column('teams',style='magenta')
    table.add_column('goals',justify='right',style='green')
    table.add_column('assists',justify='right',style='green')
    table.add_column('points',justify='right',style='green')

    return table

def get_info(season,nationality):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)
    return players

def add_players_to_table(table,players):
    for player in players:
        table.add_row(player.name,player.team,
                      str(player.goals),str(player.assists),
                      str(player.assists+player.goals))

def main():
    season=ask_season()

    nationality=ask_nationality()

    console=Console()
    table=create_table(season,nationality)

    players=get_info(season,nationality)

    add_players_to_table(table,players)

    console.print(table)



if __name__ == "__main__":
    main()
