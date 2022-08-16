import pytest
from pytest_mock import MockerFixture

from bunker import generator


@pytest.fixture(scope='session')
def fake_game_generator(session_mocker: MockerFixture):
    generator_mock = session_mocker.patch.object(generator, 'generate_game')
    return generator_mock


@pytest.fixture(scope='session')
def cli_create_line():
    return 'create -p 2 --name test'


@pytest.fixture(scope='session')
def cli_create_line_invalid():
    return 'create -p no valid args here!'


@pytest.fixture(scope='session')
def fake_deck():
    fields = [
        'professions',
        'bio',
        'goods',
        'health',
        'hobby',
        'facts',
        'catastrophes',
        'bunkers',
        'threats',
        'specials'
    ]
    return {
        field: {'items': [f'test_{field}_1', f'test_{field}_2']} for field in fields
    }
