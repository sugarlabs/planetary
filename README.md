Planetary
=========

Solar system game for the XO PC. Teaches kids about the arrangment of the solar system, and about the planets themselves.


File Explanations
=================


###PlanetaryActivity.py (Entry point)

Handles basic sugar activity things, like the toolbar and read_file/write_file


###Planetary.py (Pygame App)

Handles primary game logic and UI.


###init_data.json (question set / game state)

Written in JSON, information is organized by question. Each question can have multiple answers. The "live" properties indicate which answers (and therefore, questions) are in play. This file is only used for starting a game. Once a game is started and saved, the instance JSON (game state) is saved to the journal.
