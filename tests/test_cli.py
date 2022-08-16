from unittest.mock import MagicMock

from typer.testing import CliRunner

from bunker.__main__ import app

runner = CliRunner()


def test_create_no_args():
    result = runner.invoke(app, ['create'])
    assert result.exit_code == 2
    assert 'Error: Missing option \'--players\' / \'-p\'.' in result.stdout


def test_create_valid_args(
    fake_game_generator: MagicMock, cli_create_line: str
):
    result = runner.invoke(app, cli_create_line.split())
    assert result.exit_code == 0
    fake_game_generator.assert_called_once()


def test_create_invalid_args(cli_create_line_invalid: str):
    result = runner.invoke(app, cli_create_line_invalid.split())
    assert result.exit_code == 2
    assert 'Invalid value for \'--players\' / \'-p\': \'no\' is not a valid integer.' in result.stdout


def test_update_no_args():
    result = runner.invoke(app, ['update'])
    assert result.exit_code == 0
