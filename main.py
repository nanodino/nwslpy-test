import nwslpy
import pandas as pd
import datetime as dt

last_season = str(dt.date.today().year - 1)
this_season = str(dt.date.today().year)

all_teams = nwslpy.load_teams()
active_teams = (all_teams[all_teams["last_season"].astype(str)==this_season]).reset_index()

idx = {name: i for i, name in enumerate(list(active_teams), start = 0)}
each_team_stats = {}
each_team_player_stats = {}


for team in active_teams.itertuples(index=False):
    abbreviation = team[idx["team_abbreviation"]]
    each_team_stats[abbreviation] = nwslpy.load_team_season_stats(abbreviation, this_season).reset_index()
    each_team_player_stats[abbreviation] = nwslpy.load_player_season_stats(abbreviation, this_season).reset_index()

    team_stats_columns = list(each_team_stats[abbreviation].columns)
    player_stats_columns = list(each_team_player_stats[abbreviation].columns)
    difference = list(set(team_stats_columns) - set(player_stats_columns))

    print(f'Team: {abbreviation}. There are {len(team_stats_columns)} team stats columns and {len(player_stats_columns)} player stats columns. {len(difference)} of them are different.')
    print(f'Differences between frames for {abbreviation}: {pd.testing.assert_frame_equal(each_team_stats[abbreviation], each_team_player_stats[abbreviation])}')

