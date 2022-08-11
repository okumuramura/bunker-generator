import random
from pathlib import Path
from typing import Any, Dict, List, Optional
import os
import uuid

from bunker import logger, templates

DEFAULT_LAYOUT = {
    'player': {
        'professions': 1,
        'bio': 1,
        'goods': 2,
        'health': 1,
        'hobby': 1,
        'facts': 1,
        'specials': 1,
    },
    'board': {'catastrophes': 1, 'bunkers': 1, 'threats': 2},
}


def generate_players(
    players: int, deck: Dict[str, Any]
) -> List[Dict[str, str]]:

    options: Optional[Dict[str, Any]] = deck.get('options')

    if options is not None:
        layout: Dict[str, int] = options.get('layout', DEFAULT_LAYOUT)
    else:
        layout = DEFAULT_LAYOUT

    profiles = [{} for _ in range(players)]

    for field, num in layout['player'].items():
        data = random.sample(deck.get(field)['items'], players * num)
        field_name = deck.get(field).get('label', field)
        for player in range(players):
            profiles[player][field_name] = data[
                player * num : (player + 1) * num
            ]

    return profiles


def generate_board(deck: Dict[str, Any]) -> Dict[str, List[str]]:
    options: Optional[Dict[str, Any]] = deck.get('options')

    if options is not None:
        layout: Dict[str, int] = options.get('layout', DEFAULT_LAYOUT)
    else:
        layout = DEFAULT_LAYOUT

    board = {}

    for field, num in layout['board'].items():
        field_name = deck.get(field).get('label', field)
        board[field_name] = random.sample(deck.get(field)['items'], num)

    return board


def generate_game(
    players: int,
    deck: Dict[str, Any],
    output: Path,
    format: str = 'html',
    language: str = 'en',
    game_name: Optional[str] = None,
) -> None:

    if not output.exists() or not output.is_dir():
        output.mkdir(parents=True, exist_ok=True)

    if game_name is None:
        game_id = str(uuid.uuid4())[:8]
    else:
        game_id = game_name
    game_path = output / f'game_{game_id}'

    logger.info('Creating game %s at %s', game_id, game_path.absolute())
    game_path.mkdir(exist_ok=True)

    profiles = generate_players(players, deck)
    board = generate_board(deck)

    profile_template = templates.get_template('profile.html')
    for pid, player in enumerate(profiles, start=1):
        with open(
            game_path / f'player_{pid}.html', 'w', encoding='utf-8'
        ) as file:
            file.write(profile_template.render(profile=player))

    board_template = templates.get_template('board.html')
    with open(game_path / 'board.html', 'w', encoding='utf-8') as file:
        file.write(board_template.render(board=board))
