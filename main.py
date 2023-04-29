import nwslpy

matches = nwslpy.load_matches()
this_season_matches = matches[matches["year"]==2023]
print(this_season_matches)