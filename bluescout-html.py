#!/bin/python3

# scouting script made by connor from team 6918

# set up tbapy module https://github.com/frc1418/tbapy
import tbapy
tba = tbapy.TBA(input('Enter your TBA API key. You can get this at https://www.thebluealliance.com/account\n\n'))
key = True

# edit these variables as you like. they depend on what event you're at, what team you're in, etc.
# comp - the event ID. it's shown in the event's URL on TBA.
# us: the team that you want to focus on
comp = input("\nWhat is the ID of event are you scouting for? You can find the ID in the event's URL on TBA.\n\nExample: the ID for the 2023 Las Vegas Regional is 2023nvlv\n\n")
us = 'frc' + input("What is your team number?\n\n")

# variables to make stuff easier/abbreviated
# don't edit these unless you know what you're doing
event = tba.event(comp)
eventMatches = tba.event_matches(comp)
matchAmount = len(tba.event_matches(comp))

# variables to generate the txt file
# don't edit these unless you know what you're doing
txt = open("%s_matches.html" % (comp), "w")
addtxt = open("%s_matches.html" % (comp), "a")
txt.write("<html>\n<body>\n")
addtxt.write("<h1>Matches for %s with team %s</h1>\n\n" % (comp, us[3:]))

matchNo = 1
while matchNo < matchAmount:
    match = eventMatches[matchNo]
    blue = match.alliances['blue']
    red = match.alliances['red']
    bTeams = blue['team_keys']
    rTeams = red['team_keys']

    if us in blue['team_keys']:
       addtxt.write('<h2>Match %s</h2>\n' % (match.match_number))

       addtxt.write('<p style="color:blue"><strong>With:</strong> ')
       addtxt.write('%s, %s, %s</p>\n' % (str(bTeams[0])[3:], str(bTeams[1])[3:], str(bTeams[2])[3:]))

       addtxt.write('<p style="color:red"><strong>Against:</strong> ')
       addtxt.write('%s, %s, %s</p>\n' % (str(rTeams[0])[3:], str(rTeams[1])[3:], str(rTeams[2])[3:]))

    if us in red['team_keys']:
       addtxt.write('<h2>Match %s</h2>\n' % (match.match_number))

       addtxt.write('<p style="color:red"><strong>With:</strong> ')
       addtxt.write('%s, %s, %s</p>\n' % (str(rTeams[0])[3:], str(rTeams[1])[3:], str(rTeams[2])[3:]))

       addtxt.write('<p style="color:blue"><strong>Against:</strong> ')
       addtxt.write('%s, %s, %s</p>\n' % (str(bTeams[0])[3:], str(bTeams[1])[3:], str(bTeams[2])[3:]))

    matchNo += 1

addtxt.write("</body>\n</html>")
print('Done!')
