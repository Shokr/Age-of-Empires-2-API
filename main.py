"""
CloudInn Backend Engineer Task: -

- a command line program which takes an Age of Empires II unit name as a user input
and search for information about this unit then render this unit’s data to the user

__author__ = 'Muhammed Shokr <mohammedshokr2014@gmail.com>'
__version__ = 'v 1.0'

Task repo <https://github.com/Shokr/CloudInn-Task>
"""

import sqlite3

import requests
from tabulate import tabulate


def call_api(name):
    response = requests.get(
        f"https://age-of-empires-2-api.herokuapp.com/api/v1/unit/{name}"
    )
    if response.status_code == 200:
        return response.json()
    return False


def select_unit(name):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM units where name='{name}'")
    unit = cur.fetchall()
    cur.close()
    conn.close()
    return unit


def insert_unit(unit):
    name = unit["name"] if "name" in unit else ""
    description = unit["description"] if "description" in unit else ""
    expansion = unit["expansion"] if "expansion" in unit else ""
    age = unit["age"] if "age" in unit else ""
    created_in = unit["created_in"] if "created_in" in unit else ""
    cost = unit["cost"] if "cost" in unit else ""
    build_time = unit["build_time"] if "build_time" in unit else ""
    reload_time = unit["reload_time"] if "reload_time" in unit else ""
    attack_delay = unit["attack_delay"] if "attack_delay" in unit else ""
    movement_rate = unit["movement_rate"] if "movement_rate" in unit else ""
    line_of_sight = unit["line_of_sight"] if "line_of_sight" in unit else ""
    hit_points = unit["hit_points"] if "hit_points" in unit else ""
    rangex = unit["range"] if "range" in unit else ""
    attack = unit["attack"] if "attack" in unit else ""
    armor = unit["armor"] if "armor" in unit else ""
    attack_bonus = unit["attack_bonus"] if "attack_bonus" in unit else ""
    armor_bonus = unit["armor_bonus"] if "armor_bonus" in unit else ""
    search_radius = unit["search_radius"] if "search_radius" in unit else ""
    accuracy = unit["accuracy"] if "accuracy" in unit else ""
    blast_radius = unit["blast_radius"] if "blast_radius" in unit else ""

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    sql = """ INSERT INTO units(name, description, expansion, age, created_in, cost
            , build_time, reload_time, attack_delay, movement_rate, line_of_sight
            , hit_points, range , attack, armor, attack_bonus, armor_bonus, search_radius
            , accuracy, blast_radius)
                  VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
                   """.format(
        name,
        description,
        expansion,
        age,
        created_in,
        cost,
        build_time,
        reload_time,
        attack_delay,
        movement_rate,
        line_of_sight,
        hit_points,
        rangex,
        attack,
        armor,
        attack_bonus,
        armor_bonus,
        search_radius,
        accuracy,
        blast_radius,
    )

    # print(sql)

    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()
    return cur.lastrowid


def print_table(unit_list):
    print(
        tabulate(
            unit_list,
            headers = [
                "id",
                "name",
                "description",
                "expansion",
                "age",
                "created_in",
                "cost",
                "build_time",
                "reload_time",
                "attack_delay",
                "movement_rate",
                "line_of_sight",
                "hit_points",
                "range",
                "attack",
                "armor",
                "attack_bonus",
                "armor_bonus",
                "search_radius",
                "accuracy",
                "blast_radius",
            ],
            tablefmt = "fancy_grid",
        )
    )


def get_unit_info(unit_name):
    unit = select_unit(unit_name)
    unit_list = list(unit)

    if unit_list:
        print_table(unit_list)
    else:

        if call_api(unit_name):

            response_body = call_api(unit_name)
            inserted_record = insert_unit(response_body)
            print(f"INSERT RECORD [{inserted_record}]")

            unit_list = list(select_unit(unit_name))
            print_table(unit_list)
        else:
            print("ERROR .. try again.")


if __name__ == "__main__":

    while True:
        unitName = str(input("Enter Unit Name:- "))
        print(f"Age Of Empires II [{unitName} Information] ^_^ ... ")

        get_unit_info(unitName)
