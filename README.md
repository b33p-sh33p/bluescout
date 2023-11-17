# bluescout
script to help with scouting FRC events using tbapy

bluescout generates a .txt file with a list of matches at an event, putting an asterisk `*` next to the team you're in.

### dependencies
python (i recommend python 3.11. 3.12 may work, but i have not tested it)

[Download Python](https://www.python.org/downloads/)

tbapy ([repo](https://github.com/frc1418/tbapy))
```
pip install tbapy
```

### how to run
1. download bluescout.py
2. open in your preferred text editor. nano, vscode, notepad, it does not matter as long as it works.
3. change `key` in the `tba` variable to your TBA API key, which you can generate here: https://www.thebluealliance.com/account
```python
tba = tbapy.TBA('key')
```
4. change the `comp` variable to the identifier of the event you're scouting for. if you go the event's page on TBA, the identifier that you need should be in the URL.
```python
comp = '2023nvlv'
```
5. change the `us` variable to whatever team you're in. it should be in the format `frc0000`, where 0000 is your team number.
```python
us = 'frc6918'
```
6. save the file, and just run it like normal. if you're gonna be using bluescout for a lot of different events, i recommend making a specific directory for it, because bluescout generates a different file for each event.
```
python3 bluescout.py
```

### todo
:black_square_button: print data on md or html file instead of plain text

:black_square_button: only list matches that the highlighted team is in. don't separate by match, but do sort by match (requested by teammate, will be in a separate version)
