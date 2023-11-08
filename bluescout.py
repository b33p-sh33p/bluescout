#!/bin/python3

# scouting script made by connor b from team 6918 :)

# set up tbapy module https://github.com/frc1418/tbapy
# replace key with your TBA API key, which you can get at https://www.thebluealliance.com/account
import tbapy
tba = tbapy.TBA('key')
key = True

# edit these variables as you like. they depend on what event you're at, what team you're in, etc.
# comp - the event ID. it's shown in the event's URL on TBA.
# matchAmount - the amount of matches you want to list.
# us: in the file generated, there will be an asterisk by the matches this team is in.
comp = '2023nvlv'
matchAmount = 30
us = 'frc6918'

# variables to generate the txt file
# these variables shouldn't be edited. you can mess with them if you want, but i don't recommend it
txt = open("%s_matches.txt" % (comp), "w")
addtxt = open("%s_matches.txt" % (comp), "a")
txt.write("Matches for %s\n\n" % (comp))


matchNo = 1
while matchNo < (matchAmount + 1):
    match = tba.match(year=2023,event=comp,number=matchNo)
    blue = match.alliances['blue']
    red = match.alliances['red']

    print('Match', match.match_number)
    addtxt.write('Match %s\n' % (match.match_number))


    if us in blue['team_keys']:
        print("* ")
        addtxt.write('* ')
    print('Blue: ',blue['team_keys'])
    addtxt.write('Blue: %s\n' % (blue['team_keys']))

    if us in red['team_keys']:
        print("* ")
        addtxt.write('* ')

    print('Red: ',red['team_keys'])
    addtxt.write('Red: %s\n\n' % (red['team_keys']))

    matchNo += 1