#!/bin/python3

# scouting script made by connor from team 6918

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
matchAmount = len(tba.event_matches(comp))

# variables to generate the txt file
# don't edit these unless you know what you're doing
txt = open("%s_matches.txt" % (comp), "w")
addtxt = open("%s_matches.txt" % (comp), "a")
txt.write("Matches for %s with team " % (comp))
addtxt.write("%s\n\n" % (us[3:]))

matchNo = 1
while matchNo < matchAmount:
    match = eventMatches[matchNo]
    blue = match.alliances['blue']
    red = match.alliances['red']
    bTeams = blue['team_keys']
    rTeams = red['team_keys']

    if us in blue['team_keys']:
       print('Match', match.match_number)
       addtxt.write('Match %s\n' % (match.match_number))

       addtxt.write('With: ')
       addtxt.write('%s, %s, %s\n' % (str(bTeams[0])[3:], str(bTeams[1])[3:], str(bTeams[2])[3:]))

       addtxt.write('Against: ')
       addtxt.write('%s, %s, %s\n\n' % (str(rTeams[0])[3:], str(rTeams[1])[3:], str(rTeams[2])[3:]))
       print(' ')

    if us in red['team_keys']:
       print('Match', match.match_number)
       addtxt.write('Match %s\n' % (match.match_number))

       addtxt.write('With: ')
       addtxt.write('%s, %s, %s\n' % (str(rTeams[0])[3:], str(rTeams[1])[3:], str(rTeams[2])[3:]))
       
       addtxt.write('Against: ')
       addtxt.write('%s, %s, %s\n\n' % (str(bTeams[0])[3:], str(bTeams[1])[3:], str(bTeams[2])[3:]))
       print('')

    matchNo += 1
