import random
from pathlib import Path
from typing import Any, Dict, List, Optional

# from bunker import logger

DEFAULT_LAYOUT = {
    "player": {
        "professions": 1,
        "bio": 1,
        "goods": 2,
        "health": 1,
        "hobby": 1,
        "facts": 1,
        "specials": 1,
    },
    "board": {"catastrophes": 1, "bunkers": 1, "threats": 2},
}


def generate_players(players: int, deck: Dict[str, Any]) -> List[Dict[str, str]]:

    options: Optional[Dict[str, Any]] = deck.get("options")

    if options is not None:
        layout: Dict[str, int] = options.get("layout", DEFAULT_LAYOUT)
    else:
        layout = DEFAULT_LAYOUT

    profiles = [{} for _ in range(players)]

    for field, num in layout["player"].items():
        data = random.sample(deck.get(field), players * num)
        for player in range(players):
            profiles[player][field] = data[player * num : (player + 1) * num]

    return profiles


def generate_board(deck: Dict[str, Any]) -> Dict[str, List[str]]:
    options: Optional[Dict[str, Any]] = deck.get("options")

    if options is not None:
        layout: Dict[str, int] = options.get("layout", DEFAULT_LAYOUT)
    else:
        layout = DEFAULT_LAYOUT

    board = {}

    for field, num in layout["board"].items():
        board[field] = random.sample(deck.get(field), num)

    return board


def generate_game(
    players: int, deck: Dict[str, Any], output: Path, format: str = "html"
) -> None:
    pass
