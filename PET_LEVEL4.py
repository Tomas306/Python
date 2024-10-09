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
        if count == 1:
            return f"{count} sušienka"
        elif 2 <= count <= 4:
            return f"{count} sušienky"
        else:
            return f"{count} sušienok"
    elif item == "šunky":
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
# Hlavná funkcia pre zadanie levelov
def main():
    while True:
        print("Vyber si možnosti kŕmenia (1-5):")
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

        # Overenie aktuálneho levelu
        while True:
            print("Zadaj svoj aktuálny level (0-150):")
            current_level = int(input())
            if 0 <= current_level <= 150:
                break
            else:
                print("Neplatný level. Zadaj hodnotu medzi 0 a 150.")

        # Overenie cieľového levelu
        while True:
            print("Zadaj cieľový level (0-150, musí byť vyšší ako aktuálny level):")
            target_level = int(input())
            if 0 <= target_level <= 150 and target_level > current_level:
                break
            else:
                print(f"Neplatný cieľový level. Zadaj hodnotu medzi 0 a 150, ktorá je vyššia ako aktuálny level ({current_level}).")

        # Overenie počtu kŕmení za deň
        while True:
            print("Koľko krmení zvládneš za 24 hodín? (1-12):")
            feedings_per_day = int(input())
            if 1 <= feedings_per_day <= 12:
                break
            else:
                print("Neplatný počet krmení. Zadaj hodnotu medzi 1 a 12.")

        total_item_counts = {item: 0 for item in selected_items}
        total_calories = 0
        level_items_used = {}  # Sledovanie položiek pre jednotlivé levely

        # Sčítanie potrebných položiek pre každý level
        for level in range(current_level + 1, target_level + 1):
            if level in level_calories:
                calories = level_calories[level]
                total_calories += calories

                # Rozdelenie kalórií medzi vybrané potraviny, začínajúc od najvyššej kalórie
                remaining_calories = calories
                level_items_used[level] = {item: 0 for item in selected_items}  # Pre každý level

                # Rozdelenie kalórií podľa vybraných potravín
                for item in sorted(selected_items, key=lambda x: food_items[x], reverse=True):
                    while remaining_calories >= food_items[item]:
                        total_item_counts[item] += 1
                        level_items_used[level][item] += 1  # Sledujeme položky pre tento level
                        remaining_calories -= food_items[item]

                # Ak zostanú kalórie, pridá sa sušienka
                if remaining_calories > 0 and remaining_calories <= 15:
                    total_item_counts["sušienky"] += 1  # Pridá sušienku
                    level_items_used[level]["sušienky"] += 1  # Sledujeme sušienky pre tento level

        # Výpočet celkového krmiva potrebného a dní potrebných na krmenie
        total_feedings_needed = sum(total_item_counts[item] for item in total_item_counts)
        total_days_needed = total_feedings_needed // feedings_per_day + (total_feedings_needed % feedings_per_day > 0)

        # Výstup výsledkov
        output = []
        for item, count in total_item_counts.items():
            if count > 0:
                output.append(decline_item(item, count))

                # Výpočet počtu potrebných sušienok a ich ekvivalent
            cookie_count = total_item_counts["sušienky"]


        # Výpočet potrebných sušienok
        total_cookies_needed = 0
        for item in total_item_counts:
            if item == "pečené kura":
                total_cookies_needed += total_item_counts[item] * 81
            elif item == "steak":
                total_cookies_needed += total_item_counts[item] * 27
            elif item == "stehienko":
                total_cookies_needed += total_item_counts[item] * 9
            elif item == "šunky":
                total_cookies_needed += total_item_counts[item] * 3
            elif item == "sušienky":
                total_cookies_needed += total_item_counts[item]

        # Výpis položiek pre každý level
        print("\nPoložky použité pre jednotlivé levely:")
        for level, items in level_items_used.items():
            item_output = [decline_item(item, count) for item, count in items.items() if count > 0]
            print(f"Level {level}: {', '.join(item_output)}")

        print(f"\nNa dosiahnutie levelu {target_level} potrebujete:")
        print(", ".join(output))
        print(f"Celkové kalórie potrebné: {total_calories}.")
        print(f"Počet kŕmení potrebných: {total_feedings_needed}, čo bude trvať {total_days_needed} dní.")
        print(f"Celkový počet potrebných sušienok: {total_cookies_needed}")

        # Spýtaj sa, či chceš pokračovať
        repeat = input("Chceš pokračovať? (Y/N): ")
        if repeat.lower() != "y":
            break

# Spustenie hlavnej funkcie
main()