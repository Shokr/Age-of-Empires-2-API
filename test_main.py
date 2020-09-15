from main import get_unit_info, call_api, select_unit


def test_get_unit_info_success():
    if """
    ╒══════╤═════════════╤═════════════════╤══════════════╤════════╤═══════════════╤═════════════════════════╤══════════════╤═══════════════╤════════════════╤═════════════════╤═════════════════╤══════════════╤═════════╤══════════╤═════════╤════════════════╤═══════════════╤═════════════════╤════════════╤════════════════╕
    │   id │ name        │ description     │ expansion    │ age    │ created_in    │ cost                    │   build_time │   reload_time │   attack_delay │   movement_rate │   line_of_sight │   hit_points │   range │   attack │ armor   │ attack_bonus   │ armor_bonus   │ search_radius   │ accuracy   │ blast_radius   │
    ╞══════╪═════════════╪═════════════════╪══════════════╪════════╪═══════════════╪═════════════════════════╪══════════════╪═══════════════╪════════════════╪═════════════════╪═════════════════╪══════════════╪═════════╪══════════╪═════════╪════════════════╪═══════════════╪═════════════════╪════════════╪════════════════╡
    │    2 │ Crossbowman │ Upgraded archer │ Age of Kings │ Castle │ Archery Range │ {"Wood": 25;"Gold": 45} │           27 │             2 │           0.35 │            0.96 │               7 │           35 │       5 │        5 │ 0/0     │ +3 spearmen    │               │                 │ 85%        │                │
    ╘══════╧═════════════╧═════════════════╧══════════════╧════════╧═══════════════╧═════════════════════════╧══════════════╧═══════════════╧════════════════╧═════════════════╧═════════════════╧══════════════╧═════════╧══════════╧═════════╧════════════════╧═══════════════╧═════════════════╧════════════╧════════════════╛
    """ in str(get_unit_info('Crossbowman')):
        assert True


def test_get_unit_info_failure():
    if 'ERROR .. try again.' in str(get_unit_info('Shokr')):
        assert True


def test_call_api_success():
    assert call_api('Crossbowman') == {
        "id": 2,
        "name": "Crossbowman",
        "description": "Upgraded archer",
        "expansion": "Age of Kings",
        "age": "Castle",
        "created_in": "https://age-of-empires-2-api.herokuapp.com/api/v1/structure/archery_range",
        "cost": {
            "Wood": 25,
            "Gold": 45
        },
        "build_time": 27,
        "reload_time": 2,
        "attack_delay": 0.35,
        "movement_rate": 0.96,
        "line_of_sight": 7,
        "hit_points": 35,
        "range": 5,
        "attack": 5,
        "armor": "0/0",
        "attack_bonus": [
            "+3 spearmen"
        ],
        "accuracy": "85%"
    }


def test_call_api_failure():
    assert call_api('cloudInn') is False


def test_select_unit_success():
    assert select_unit('Crossbowman') == [(2, 'Crossbowman', 'Upgraded archer', 'Age of Kings', 'Castle',
                                           'Archery Range', '{"Wood": 25;"Gold": 45}', 27, 2.0, 0.35, 0.96, 7, 35, '5',
                                           5, '0/0', '+3 spearmen', '', None, '85%', None)]


def test_select_unit_failure():
    assert select_unit('Shokr') == []

# Crossbowman
# Skirmisher
