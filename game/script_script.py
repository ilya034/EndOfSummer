script = open("raw_script.txt", "r", encoding="UTF-8").read()

names = {"ГГ": "mc", "ГГ (В мыслях)": "mc", "Автор": "",
         "Владимир": "vladimir", "Андрей": "andrey", "Аня": "anya", "Платон": "platon"}

output = open("script.txt", "w", encoding="UTF-8")
for line in script.split("\n"):
    line_splitted = line.split(":")

    if len(line_splitted) == 1 or line_splitted[0] not in names.keys():
        continue

    name = names[line_splitted[0]]
    display_name = name if name != "mc" else "[mc_name]"
    text = line_splitted[1]

    if name: s = f"\n\nshow {name}\nwith fade\n{name} \"{text.strip().replace("*имя*", display_name)}\""
    else: s = f"\n\n\"{text[1:]}\""

    output.write(s)
