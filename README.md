# icc-loot-competition
Quick dirty script to display the loot competition in icc for our guild. BIS lists are based of this sim sheet https://docs.google.com/spreadsheets/d/e/2PACX-1vQTLPd3Wkmeb-GEjMBAOXmxX5bcnAw6aKYDnpfXFvYTI7Ni-lEjKxm52mYujPR-AeiOGEv0xaJfPukq/pubhtml

Output file is google spreadsheet friendly :)


Quick description
-----
| Folder | Description |
| --- | --- |
| loot_table | raw and formatted loot table txt files |
| wowsims_data | exports of all sims of the sheet above |

Export the json files from the sims above and insert them into wowsims_data (file ending .json). Names have to be according to the following definitions.

``` python
class_amount = {
    "dk_blood": 0,
    "dk_frost": 1,
    "dk_unholy_dw": 2,
    "druid_balance": 2,
    "druid_feral": 1,
    "druid_restoration": 1,
    "hunter_beastmastery": 0,
    "hunter_marksmanship": 1,
    "hunter_survival": 0,
    "mage_fire": 3,
    "paladin_holy": 2,
    "paladin_protection": 2,
    "paladin_retribution": 1,
    "priest_discipline": 1,
    "priest_shadow": 2,
    "rogue_assassination": 0,
    "rogue_combat": 2,
    "shaman_elemental": 2,
    "shaman_enhancement": 0,
    "shaman_restoration": 1,
    "warlock_affliction": 1,
    "warlock_demonology": 1,
    "warlock_destruction": 0,
    "warrior_arms": 0,
    "warrior_fury": 3,
    "warrior_protection": 0
}
```

