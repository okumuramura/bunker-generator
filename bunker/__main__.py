import json
from pathlib import Path
from typing import Any, Dict, Optional

from typer import Option, Typer

from bunker import generator, logger

typer = Typer()


@typer.command(help="Create bunker game with selected options")
def create(
    players: int = Option(..., "--players", "-p", help="Players count."),
    deck: Path = Option(
        "./decks/original_ru.json", "--deck", "-d", help="Deck file path."
    ),
    output_dir: Path = Option(
        "./games",
        "--output",
        "-o",
        help="Output directory where you wnat to create your game.",
    ),
    language: Optional[str] = Option(
        None,
        "--language",
        "-l",
        help="Output templates language (values depends on deck language).",
    ),
    # TODO for python3.8+ change to Literal['html', 'txt']
    format: str = Option(
        "html", "--format", "-f", help='Output format (supported "html", "txt").'
    ),
    name: Optional[str] = Option(
        None, "--name", "-n", help="Game name (random will generated if not exists)."
    ),
    ignore: bool = Option(False, "--ignore", help="Ignore deck recommendations."),
):
    logger.info("Deck file: %s", deck)
    if not deck.is_file():
        logger.error("Deck file not exists!")
        return

    deck_obj: Dict[Any] = json.load(deck.open("r", encoding="utf-8"))

    # CHECK SETTINGS
    deck_options: Optional[Dict[str, Any]] = deck_obj.get("options")

    if deck_obj is not None and not ignore:

        # PLAYERS COUNT
        min_players: int = deck_options.get("min_players", 0)
        max_players: int = deck_options.get("max_players", 100)
        if not min_players <= players <= max_players:
            logger.warning(
                "Mismatch in the number of players (%d). Expected >= %d and <= %d.",
                players,
                min_players,
                max_players,
            )

        # LANGUAGE MATCH
        option_language: Optional[str] = deck_options.get("language")
        if language is not None and option_language is not None:
            if language != option_language:
                logger.warning(
                    'Mismatch language ("%s" != "%s")', language, option_language
                )
        elif language is None and option_language is None:
            language = "en"
            logger.warning('No language selectet. Using "en"')
        elif language is None:
            language = option_language

    generator.generate_game(
        players=players, deck=deck_obj, output=output_dir, format=format, game_name=name
    )


@typer.command(help="Generate separate fields or player's profiles")
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
    profiles: int = Option(0),
):
    pass


@typer.command()
def update():
    pass


if __name__ == "__main__":
    typer()
