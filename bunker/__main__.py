from pathlib import Path
from typing import Dict, Any, Optional
import json
import pprint

from typer import Typer, Option

from bunker import logger, generator

typer = Typer()


@typer.command(help='Create bunker game with selected options')
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
            logger.warning(
                'Mismatch in the number of players (%d). Expected >= %d and <= %d.',
                players,
                min_players,
                max_players
            )

    pprint.pprint(generator.generate_players(players, deck_obj))
    pprint.pprint(generator.generate_board(deck_obj))


@typer.command(help='Generate separate fields or player\'s profiles')
def generate(
    professions: int = Option(0),
    bio: int = Option(0),
    goods: int = Option(0),
    health: int = Option(0),
    hobby: int = Option(0),
    facts: int = Option(0),
    catastrophes: int = Option(0),
    bunkers: int = Option(0),
    threats: int = Option(0),
    specials: int = Option(0),
    profiles: int = Option(0)
):
    pass


@typer.command()
def update():
    pass


if __name__ == "__main__":
    typer()
