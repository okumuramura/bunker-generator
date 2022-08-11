import logging
import os
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

os.chdir('./bunker')
WORKDIR = Path.cwd()
DECKSDIR = WORKDIR / 'decks'

__log_format = r'[%(levelname)s] %(message)s'
logger = logging.Logger(__name__, logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(__log_format))
logger.addHandler(handler)

templates = Environment(
    loader=PackageLoader(__name__, package_path='templates'),
    autoescape=select_autoescape(),
)
