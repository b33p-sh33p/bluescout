#!/bin/python3

# scouting script made by connor b from team 6918 :)

# set up tbapy module https://github.com/frc1418/tbapy
# replace key with your TBA API key, which you can get at https://www.thebluealliance.com/account
import tbapy
tba = tbapy.TBA('key')
key = True

# edit these variables as you like. they depend on what event you're at, what team you're in, etc.
# comp - the event ID. it's shown in the event's URL on TBA.
# us: in the file generated, there will be an asterisk next to the matches this team is in.
comp = '2023nvlv'
us = 'frc6918'

# variables to make stuff easier/abbreviated
# don't edit these unless you know what you're doing
event = tba.event(comp)
eventMatches = tba.event_matches(comp)
matchAmount = len(eventMatches)
ourMatches = tba.team_matches(us, comp)
ourMatchAmount = len(ourMatches)

# variables to generate the txt file
# don't edit these unless you know what you're doing
txt = open("%s_ourMatches.txt" % (comp), "w")
addtxt = open("%s_ourMatches.txt" % (comp), "a")
txt.write("Matches for %s with Team %s\n\n" % (event.name, us[3:]))


matchNo = 1
while matchNo < ourMatchAmount:
    match = ourMatches[matchNo]
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
