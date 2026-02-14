def prepare_knight(knight_data: dict) -> None:
    knight_data["protection"] = 0
    for armour_part in knight_data["armour"]:
        knight_data["protection"] += armour_part["protection"]
    knight_data["power"] += knight_data["weapon"]["power"]
    if knight_data["potion"] is not None:
        effect = knight_data["potion"]["effect"]
        if "power" in effect:
            knight_data["power"] += effect["power"]

        if "protection" in effect:
            knight_data["protection"] += effect["protection"]

        if "hp" in effect:
            knight_data["hp"] += effect["hp"]
