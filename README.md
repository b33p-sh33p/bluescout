# bluescout
Script to help with scouting FRC events using tbapy

bluescout generates a .txt or .html file (depending on what version you use) with a list of matches that your team is in at an event

### Dependencies
python (tested with versions 3.11 and 3.14)

[Download Python](https://www.python.org/downloads/)

tbapy ([repo](https://github.com/frc1418/tbapy))
```
pip install tbapy
```

### Generating files
1. Create a TBA API key at [https://www.thebluealliance.com/account]

2. Download [bluescout-txt.py](./bluescout-txt.py) or [bluescout-html.py](./bluescout-html.py) (note: the script for genetating HTML files is not complete)

3. Run bluescout-txt.py or bluescout-html.py - It's recommended to run the script in a specific directory because it generates a new file for every event.

When you run the script, it'll ask you for the API key that you generated in step 1. It'll also ask for the specific event ID, which can be found in the URL for the event on TBA:

![Screenshot of the TBA page for the CA District East Bay Event of 2026, with a red circle around and an arrow pointing to the part of the URL with the event ID, which is 2026caetb.](./event-id-example.jpg "Example of an event ID")

### Todo
- Print data on .md or html file instead of plain text (html in progress)
