# Bunker

Bunker-like role-play game generator.
> Disclaimer: this app only generates player's profiles and has no tools for holding a game. For the game you need a leader who will control everything.


## Requirements
```bash
pip install -r requirements.txt
# OR
poetry install
```

## Generate game
```
python -m bunker create [OPTIONS]

Options:
  -p, --players INTEGER  Players count.  [required]
  -d, --deck PATH        Deck file path.  [default: ./decks/original_ru.json]
  -o, --output PATH      Output directory where you want to create your game.
                         [default: ./games]
  -l, --language TEXT    Output templates language (values depends on deck
                         language).
  -f, --format TEXT      Output format (supported "html", "txt").  [default:
                         html]
  -n, --name TEXT        Game name (random will generated if not exists).
  --ignore               Ignore deck recommendations.
  --help                 Show this message and exit.
```

Generated game will locate in \<output path\>/game_\<game name\>.

Game structure looks like that:
```
BUNKER-GENERATOR\BUNKER\GAMES
├───game_1d3edbd6
│       board.html
│       player_1.html
│       player_2.html
│
└───game_7a72f5d7
        board.html
        player_1.html
        player_2.html
        player_3.html
        player_4.html
        player_5.html

```

## Customization
You can flexible customize game files like decks and templates.

### Decks
Decks files stored in json format at `bunker/decks`. You can use default decks for creating your own.  
Deck file can contains `options` block that determinate suggested options for that deck (for example players number or language). Also `options` block contains layout block that controls how much cards will at board and player's hands.  
Options example:
```json
"options": {
    "min_players": 2,
    "max_players": 16,
    "language": "en",
    "layout": {
        "player": {
          "professions": 1,
          "bio": 1,
          "goods": 1,
          "health": 1,
          "hobby": 1,
          "facts": 1,
          "specials": 1
        },
        "board": {
          "catastrophes": 1,
          "bunkers": 5,
          "threats": 2
        }
    }
```
You can change that values to make your own deck with your own rules.
Other blocks are sub-decks with cards. They can have `label` and `hide` field. Cards stored under `items` field.  
Cards can be two different types - simple and named. Simple cards are strings with text. Named cards contains two fields: `title` and `description`.

### Templates
Templates created via [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) syntax. Default templates stored at `bunker/templates`. You can change them or create your own. Use default templates as example.
