import os


def parse_line(raw_line):
    return raw_line.strip().replace("*имя*", "[mc_name]")


def preparse(raw_text):
    replace_list = {"BackGround": "BG"}

    for key in replace_list:
        raw_text = raw_text.replace(key, replace_list[key])

    return raw_text


names = {
    "гг": "mc",
    "гг (в мыслях)": "mc_thoughts",
    "автор": "",
    "владимир": "vladimir",
    "андрей": "andrey",
    "аня": "anya",
    "платон": "platon"
}

bgs = {
    "black": "black",
    "guk": "guk",
    "радик": "rtf",
    "collegetown": "collegetown",
    "dormitorycorridor": "dormitory_corridor",
    "room": "dormitory_room",
    "trainstation": "railway_station",
    "phone1": "phone1",
    "phone2": "phone2",
    "phone": "phone",
    "mirror": "mirror"
}

sfxs = {
    "": ""
}

base_path = os.path.abspath(os.getcwd()) + "\\script\\raw_script\\"
script = preparse(open(base_path + "raw_script.txt", "r", encoding="UTF-8").read())

time = 0

output = open(base_path + "script.txt", "w", encoding="UTF-8")
for raw_line in script.split("\n"):
    line_splitted = raw_line.split(":")

    parsed_line = str()
    if len(line_splitted) == 1:
        parsed_line = f"\n\nshow text \"{line_splitted[0]}\" at truecenter"
    else:
        command = line_splitted[0].lower()
        line = parse_line(line_splitted[1])

        if command in names.keys():
            time += len(line.split()) / 175

            name = names[command]
            if name == "mc_thoughts":
                parsed_line = f"\n\nmc \"{line}\" with mc_thoughts"
            elif name == "":
                parsed_line = f"\n\n\"{line}\""
            else:
                parsed_line = f"\n\nshow {name if name != "mc_thoughts" else "mc"} at left\n{name} \"{line}\""

        elif command == "bg":
            try:
                parsed_line = f"\n\nshow {bgs[line.lower().split()[0]]}"
            except:
                parsed_line = f"\n\nshow text \"хуйня: пиздить гей дизайнера за строку: {line}\""

    output.write(parsed_line)

output.close()
print(time)
