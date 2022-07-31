from pathlib import Path
import logging

WORKDIR = Path.cwd()
DECKSDIR = WORKDIR / "decks"

__log_format = r'[%(levelname)s] - %(name)s - %(message)s'
logger = logging.Logger(__name__, logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(__log_format))
logger.addHandler(handler)
