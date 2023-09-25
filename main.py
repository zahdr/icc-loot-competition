import json
import os

def build_needed_item_list(class_amount):
    all_needed_item_ids = []
    needed_item_amount = {}

    for wowsims_file in os.listdir('wowsims_data'):
        with open(f'wowsims_data/{wowsims_file}') as f:
            f_jsonify = json.load(f)
            for i in range(class_amount[wowsims_file.split(".")[0]]):
                for j in f_jsonify["player"]["equipment"]["items"]:
                    if j: all_needed_item_ids.append(j["id"])
                
    needed_item_ids = list(set(all_needed_item_ids))

    for i in needed_item_ids:
        needed_item_amount[str(i)] = all_needed_item_ids.count(i)

    return needed_item_amount


def fetch_bosses():
    bosses = []

    with open("loot_table/loot_table_formatted.txt", "r") as f:
        for line in f:
            boss_name = line.split(";")[0]
            if boss_name not in bosses:
                bosses.append(boss_name)
    return bosses


def build_loot_table():
    loot_table = {}

    with open("loot_table/loot_table_formatted.txt", "r") as f:
        for line in f:
            l = line.split(";")
            if l[0] not in loot_table:
                loot_table[l[0]] = [l[1]]
            else:
                loot_table[l[0]].append(l[1])

    return loot_table


def translate_id_to_name():
    translated_id = {}

    with open("loot_table/loot_table_formatted.txt", "r") as f:
        for line in f:
            translated_id[line.split(";")[1]] = line.split(";")[2][:-1]
    
    return translated_id



if __name__ == "__main__":
    class_amount = {
        "dk_blood": 0,
        "dk_frost": 0,
        "dk_unholy_dw": 0,
        "druid_balance": 0,
        "druid_feral": 1,
        "druid_restoration": 0,
        "hunter_beastmaster": 0,
        "hunter_marksmanship": 0,
        "hunter_survival": 0,
        "mage_fire": 0,
        "paladin_holy": 0,
        "paladin_protection": 0,
        "paladin_retribution": 0,
        "priest_discipline": 0,
        "priest_shadow": 0,
        "rogue_assassinatoin": 0,
        "rogue_combat": 0,
        "shaman_elemental": 0,
        "shaman_enhancer": 0,
        "shaman_restoration": 0,
        "warlock_affliction": 0,
        "warlock_demonology": 0,
        "warlock_destruction": 0,
        "warrior_arms": 0,
        "warrior_fury": 3,
        "warrior_protection": 0
    }

    item_list = build_needed_item_list(class_amount) #dict
    bosses = fetch_bosses() #dict
    loot_table = build_loot_table() #dict
    translated_id = translate_id_to_name() #dict

    with open("output.txt", "w") as f:
        for boss in bosses:
            if loot_table[boss]:
                for item in loot_table[boss]:
                    if item in item_list:
                        f.write(f"{boss};{translated_id[item]};{item_list[item]}\n")


    