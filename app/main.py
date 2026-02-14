from .knights.knights import KNIGHTS
from .preparations.battle_preparations import prepare_knight
from .combat import fight


def battle(knights_config: dict) -> dict:
    for knight_id in knights_config:
        prepare_knight(knights_config[knight_id])

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    fight(lancelot, mordred)

    fight(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
