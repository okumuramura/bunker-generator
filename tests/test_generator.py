from bunker import generator


def test_generate_players(fake_deck):
    result = generator.generate_players(
        players=1,
        deck=fake_deck
    )

    assert len(result) == 1
    assert result[0].get('bio').get('cards')[0].startswith('test_bio_')
    assert result[0].get('professions').get('hide') is False
    assert result[0].get('goods').get('label') == 'goods'


def test_generate_board(fake_deck):
    result = generator.generate_board(
        deck=fake_deck
    )

    assert result.get('bunkers').get('cards')[0].startswith('test_bunkers_')
    assert len(result.get('threats').get('cards')) == 2
    assert result.get('threats').get('cards')[0].startswith('test_threats_')
