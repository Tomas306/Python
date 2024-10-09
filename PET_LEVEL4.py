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

# Definovanie kalórií pre jednotlivé položky
food_items = {
    "pečené kura": 240,
    "steak": 120,
    "stehienko": 60,
    "šunky": 30,
    "sušienky": 15
}


# Funkcia pre výber potravín
def get_selected_food(choice):
    if choice == 1:
        return ["sušienky"]
    elif choice == 2:
        return ["šunky", "sušienky"]
    elif choice == 3:
        return ["stehienko", "šunky", "sušienky"]
    elif choice == 4:
        return ["steak", "stehienko", "šunky", "sušienky"]
    elif choice == 5:
        return ["pečené kura", "steak", "stehienko", "šunky", "sušienky"]
    else:
        return []


# Funkcia pre skloňovanie
def decline_item(item, count):
    if item == "sušienky":
        return f"{count} sušienka" if count == 1 else f"{count} sušienok"
    elif item == "šunky":
        return f"{count} šunka" if count == 1 else f"{count} šuniek"
    elif item == "stehienko":
        return f"{count} stehienko" if count == 1 else f"{count} stehienok"
    elif item == "steak":
        return f"{count} steak" if count == 1 else f"{count} steakov"
    elif item == "pečené kura":
        return f"{count} pečené kura" if count == 1 else f"{count} pečených kurčiat"


# Hlavná funkcia pre zadanie levelov
def main():
    while True:
        print("Vyber si možnosti kŕmenia:")
        print("1 - Sušienky")
        print("2 - Sušienky a šunky")
        print("3 - Sušienky, šunky a stehienko")
        print("4 - Sušienky, šunky, stehienko a steak")
        print("5 - Sušienky, šunky, stehienko, steak a pečené kura")

        choice = int(input("Zvoľ si číslo možnosti: "))
        selected_items = get_selected_food(choice)

        # Kontrola, či bola zvolená platná možnosť
        if not selected_items:
            print("Neplatná voľba. Zvoľ prosím možnosť od 1 do 5.")
            continue  # Opakuj cyklus, ak je voľba neplatná

        print("Zadaj svoj aktuálny level:")
        current_level = int(input())

        print("Zadaj cieľový level:")
        target_level = int(input())

        print("Koľko krmení zvládneš za 24 hodín?")
        feedings_per_day = int(input())

        total_item_counts = {item: 0 for item in selected_items}
        total_calories = 0

        # Sčítanie potrebných položiek pre každý level
        for level in range(current_level + 1, target_level + 1):
            if level in level_calories:
                calories = level_calories[level]
                total_calories += calories

                # Rozdelenie kalórií medzi vybrané potraviny, začínajúc od najvyššej kalórie
                remaining_calories = calories

                # Rozdelenie kalórií podľa vybraných potravín
                for item in sorted(selected_items, key=lambda x: food_items[x], reverse=True):
                    while remaining_calories >= food_items[item]:
                        total_item_counts[item] += 1
                        remaining_calories -= food_items[item]

                # Ak zostanú kalórie, pridá sa sušienka
                if remaining_calories > 0 and remaining_calories <= 15:
                    total_item_counts["sušienky"] += 1  # Pridá sušienku

        # Výpočet celkového krmiva potrebného a dní potrebných na krmenie
        total_feedings_needed = sum(total_item_counts[item] for item in total_item_counts)
        total_days_needed = total_feedings_needed // feedings_per_day + (total_feedings_needed % feedings_per_day > 0)

        # Výstup výsledkov
        output = []
        for item, count in total_item_counts.items():
            if count > 0:
                output.append(decline_item(item, count))

        print(f"Na dosiahnutie levelu {target_level} potrebujete:")
        print(", ".join(output))
        print(f"Celkové kalórie potrebné: {total_calories}.")

        # Ukončenie programu po vykonaní výpočtov
        input("Stlač Enter na ukončenie programu...")
        break  # Ukončite program po vykonaní výpočtov


# Spustenie hlavnej funkcie
main()
