# Definovanie kalórií pre jednotlivé levely
level_calories = {
    0: 0, 1: 55, 2: 60, 3: 65, 4: 70, 5: 75, 6: 80, 7: 85,
    8: 90, 9: 95, 10: 100, 11: 105, 12: 110, 13: 115, 14: 120,
    15: 125, 16: 130, 17: 135, 18: 140, 19: 145, 20: 150, 21: 155,
    22: 160, 23: 165, 24: 170, 25: 175, 26: 180, 27: 185, 28: 190,
    29: 195, 30: 200, 31: 205, 32: 210, 33: 215, 34: 220, 35: 225,
    36: 230, 37: 235, 38: 240, 39: 245, 40: 250, 41: 255, 42: 260,
    43: 265, 44: 270, 45: 275, 46: 280, 47: 285, 48: 290, 49: 295,
    50: 300, 51: 305, 52: 310, 53: 315, 54: 320, 55: 325, 56: 330,
    57: 335, 58: 340, 59: 345, 60: 350, 61: 355, 62: 360, 63: 365,
    64: 370, 65: 375, 66: 380, 67: 385, 68: 390, 69: 395, 70: 400,
    71: 405, 72: 410, 73: 415, 74: 420, 75: 425, 76: 430, 77: 435,
    78: 440, 79: 445, 80: 450, 81: 455, 82: 460, 83: 465, 84: 470,
    85: 475, 86: 480, 87: 485, 88: 490, 89: 495, 90: 500, 91: 505,
    92: 510, 93: 515, 94: 520, 95: 525, 96: 530, 97: 535, 98: 540,
    99: 545, 100: 550, 101: 555, 102: 560, 103: 565, 104: 570, 105: 575,
    106: 580, 107: 585, 108: 590, 109: 595, 110: 600, 111: 605, 112: 610,
    113: 615, 114: 620, 115: 625, 116: 630, 117: 635, 118: 640, 119: 645,
    120: 650, 121: 655, 122: 660, 123: 665, 124: 670, 125: 675, 126: 680,
    127: 685, 128: 690, 129: 695, 130: 700, 131: 705, 132: 710, 133: 715,
    134: 720, 135: 725, 136: 730, 137: 735, 138: 740, 139: 745, 140: 750,
    141: 755, 142: 760, 143: 765, 144: 770, 145: 775, 146: 780, 147: 785,
    148: 790, 149: 795, 150: 800,
}
item_to_cookie_conversion = {
    "pečené kura": 81,
    "steak": 27,
    "stehienko": 9,
    "šunka": 3,
    "sušienky": 1  # sušienky ostávajú 1:1
}
# Definovanie kalórií pre jednotlivé položky v drahej verzii
expensive_food_items = {
    "pečené kura": 240,
    "steak": 120,
    "stehienko": 60,
    "šunka": 30,
    "sušienky": 15
}


# Definovanie kalórií pre jednotlivé položky v lacnejšej verzii
cheap_food_items = {
    "pečené kura": 240,
    "steak": 120,
    "stehienko": 60,
    "šunka": 30,
    "sušienky": 15
}
def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Prosím, zadajte hodnotu v rozsahu {valid_range}")
        except ValueError:
            print("Neplatný vstup. Skúste to znova.")

# Funkcia pre výber potravín
def get_selected_food(choice, expensive_version):
    if expensive_version:
        if choice == 1:
            return ["stehienko"]
        elif choice == 2:
            return ["steak", "stehienko"]
        elif choice == 3:
            return ["pečené kura", "steak", "stehienko"]
    else:
        if choice == 1:
            return ["sušienky"]
        elif choice == 2:
            return ["šunka", "sušienky"]
        elif choice == 3:
            return ["stehienko", "šunka", "sušienky"]
        elif choice == 4:
            return ["steak", "stehienko", "šunka", "sušienky"]
        elif choice == 5:
            return ["pečené kura", "steak", "stehienko", "šunka", "sušienky"]
    return []

# Funkcia pre skloňovanie
def decline_item(item, count):
    if item == "sušienky":
        if count == 1:
            return f"{count} sušienka"
        elif 2 <= count <= 4:
            return f"{count} sušienky"
        else:
            return f"{count} sušienok"
    elif item == "šunka":
        if count == 1:
            return f"{count} šunka"
        elif 2 <= count <= 4:
            return f"{count} šunky"
        else:
            return f"{count} šuniek"
    elif item == "stehienko":
        if count == 1:
            return f"{count} stehienko"
        elif 2 <= count <= 4:
            return f"{count} stehienka"
        else:
            return f"{count} stehienok"
    elif item == "steak":
        if count == 1:
            return f"{count} steak"
        elif 2 <= count <= 4:
            return f"{count} steaky"
        else:
            return f"{count} steakov"
    elif item == "pečené kura":
        if count == 1:
            return f"{count} pečené kura"
        elif 2 <= count <= 4:
            return f"{count} pečené kurčatá"
        else:
            return f"{count} pečených kurčiat"

# Funkcia pre krmenie jednotlivých levelov
def feed_levels(current_level, desired_level, selected_items, is_expensive, feedings_per_day):
    print("\nPlán kŕmenia pre jednotlivé levely:")

    # Pridajte 'sušienky' do vybraných položiek, ak nie je zahrnuté
    if 'sušienky' not in selected_items:
        selected_items.append('sušienky')

    total_item_counts = {item: 0 for item in selected_items}
    level_items_used = {}

    for level in range(current_level + 1, desired_level + 1):
        if level in level_calories:
            calories = level_calories[level]
            remaining_calories = calories
            level_items_used[level] = {item: 0 for item in selected_items}  # Pre každý level

            # Rozdelenie kalórií medzi vybrané potraviny
            for item in sorted(selected_items, key=lambda x: (
                expensive_food_items.get(x, 0) if is_expensive else cheap_food_items.get(x, 0)), reverse=True):
                while remaining_calories >= (expensive_food_items[item] if is_expensive else cheap_food_items[item]):
                    total_item_counts[item] += 1
                    level_items_used[level][item] += 1
                    remaining_calories -= (expensive_food_items[item] if is_expensive else cheap_food_items[item])

            # Pridanie sušienok a šunky len ak zostanú kalórie
            if is_expensive and remaining_calories > 31 and remaining_calories <= 60:
                item = "stehienko"
                total_item_counts[item] += 1
                level_items_used[level][item] += 1
            elif is_expensive and remaining_calories > 16 and remaining_calories <= 30:
                item = "šunka"
                total_item_counts[item] += 1
                level_items_used[level][item] += 1
            elif is_expensive and remaining_calories < 15:
                item = "sušienky"
                total_item_counts[item] += 1
                level_items_used[level][item] += 1
            elif not is_expensive and remaining_calories > 0 and remaining_calories <= 15:
                item = "sušienky"
                total_item_counts[item] += 1
                level_items_used[level][item] += 1

    # Výpočet celkového počtu použitých položiek
    total_items_used = sum(total_item_counts.values())

    # Výpočet počtu dní potrebných na krmenie
    total_feedings_needed = total_items_used // feedings_per_day
    total_feedings_needed += (total_items_used % feedings_per_day > 0)

    # Výpočet celkového počtu sušienok
    total_cookies = 0
    for item, count in total_item_counts.items():
        total_cookies += count * item_to_cookie_conversion.get(item, 0)

    # Výpis výsledkov
    for level in range(current_level + 1, desired_level + 1):
        if level in level_items_used:
            print(f"Level {level}:")
            for item, count in level_items_used[level].items():
                if count > 0:
                    print(f" - {decline_item(item, count)}")

    print("\nCelkové množstvo použitých položiek:")
    for item, count in total_item_counts.items():
        if count > 0:
            print(f"{decline_item(item, count)}")

    print(f"\nPočet dní krmenia: {total_feedings_needed}")
    print(f"Celkový počet použitých položiek: {total_items_used}")
    print(f"Celkový počet sušienok: {total_cookies}")

# Hlavná funkcia pre zadanie levelov
def main():
    while True:
        # Výber verzie krmiva
        expensive_version_input = get_valid_input("Vyberte si verziu krmiva: 1. Lacná 2. Drahá (zadajte 1 alebo 2): ", [1, 2])
        is_expensive = expensive_version_input == 2

        # Výber kombinácie potravín
        if is_expensive:
            food_choice = get_valid_input(
                "Vyberte si kombináciu potravín: \n 1. Drahá 1 (stehienko)\n 2. Drahá 2 (steak + stehienko)\n 3. Drahá 3 (pečené kura + steak + stehienko): ",
                [1, 2, 3]
            )
        else:
            food_choice = get_valid_input(
                "Vyberte si kombináciu potravín: \n 1. Lacná 1 (sušienky)\n 2. Lacná 2 (šunka + sušienky)\n 3. Lacná 3 (stehienko + šunka + sušienky)\n 4. Lacná 4 (steak + stehienko + šunka + sušienky)\n 5. Lacná 5 (pečené kura + steak + stehienko + šunka + sušienky): ",
                [1, 2, 3, 4, 5]
            )

        selected_items = get_selected_food(food_choice, is_expensive)

        # Získanie aktuálneho a požadovaného levelu
        current_level = get_valid_input("Zadajte váš aktuálny level (0 - 150): ", range(0, 150))
        desired_level = get_valid_input("Zadajte požadovaný level (1 - 150, musí byť väčší ako aktuálny level): ", range(current_level + 1, 151))

        # Počet krmení za deň
        feedings_per_day = get_valid_input("Zadajte počet kŕmení za deň (0 - 12): ", range(0, 13))

        # Výpočet kŕmení
        feed_levels(current_level, desired_level, selected_items, is_expensive, feedings_per_day)

        # Opakovať proces alebo skončiť
        repeat = input("Chcete pokračovať? (y/n): ").strip().lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()