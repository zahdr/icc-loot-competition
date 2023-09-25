
output = []
with open("loot_table/loot_table_raw.txt", "r") as f:
    for line in f:
        current_line = line.split(";")
        if current_line[0] == "\"Icecrown Citadel H25\"":
            if current_line[1][0] == "\"":
                boss = current_line[1][1:-1]
            else:
                boss = current_line[1]

            if current_line[2][0] == "\"":
                item_name = current_line[2][1:-1]
            else:
                item_name = current_line[2]
                
            item_id = current_line[4]
            output.append(f"{boss};{item_id};{item_name}")

with open("loot_table/loot_table_formatted.txt", "w") as f:
    for i in output:
        f.write(i + "\n")