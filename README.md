# Bunker

Bunker-like role-play game generator.


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
  -o, --output PATH      Output directory where you wnat to create your game.
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

