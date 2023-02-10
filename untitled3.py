# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:33:25 2023

@author: n1162608
"""

# opening the .txt using try and finally
try:
    f = open("epl.txt","r")

    content = f.read()
    teams_list = content.split("\n") # creating a list by splitting each line
finally:
    f.close()

# Team class
class Team:
    def __init__(self, clubname, stadium, city):
        self.club = clubname
        self.homeground = stadium
        self.city = city

teams_list_final = []


for team in teams_list:
    
    team_name_ls = team.split(":")
    team_name = team_name_ls[0]
    
    team_stadium_ls = team_name_ls[1].split("-")
    team_stadium = team_stadium_ls[0]
    
    team_area = team_stadium_ls[1]
    
    teams_dict = {"Club": team_name, "Stadium": team_stadium, "City": team_area}
    teams_list_final.append(teams_dict)

t = []
for team in teams_list_final:  
    t.append(Team(team["Club"],team["Stadium"],team["City"]))

print(t[-1].club,t[2].homeground)