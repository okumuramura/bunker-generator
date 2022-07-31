from pathlib import Path
from typing import Dict, Any, Optional
import json

from typer import Typer, Option

from bunker import logger

typer = Typer()


@typer.command()
def create(
    players: int = Option(
        ...,
        "--players",
        "-p",
        help='Players count.'
    ),
    deck: Path = Option(
        "./decks/original_ru.json",
        "--deck",
        "-d",
        help='Deck file path.'
    ),
    ignore: bool = Option(
        False,
        '--ignore',
        help='Ignore deck recommendations.'
    )
):
    logger.info('deck file: %s', deck)
    if not deck.is_file():
        logger.error('Deck file not exists!')
        return

    deck_obj: Dict[Any] = json.load(deck.open('r', encoding='utf-8'))

    # CHECK SETTINGS
    deck_options: Optional[Dict[str, Any]] = deck_obj.get('options')

    if deck_obj is not None and not ignore:

        # PLAYERS COUNT
        min_players: int = deck_options.get('min_players', 0)
        max_players: int = deck_options.get('max_players', 100)
        if not min_players <= players <= max_players:
            logger.error(
                'Invalid players count: %d. Required: %d<=players<=%d',
                players,
                min_players,
                max_players
            )


@typer.command()
def generate():
    pass


@typer.command()
def update():
    pass


if __name__ == "__main__":
    typer()
