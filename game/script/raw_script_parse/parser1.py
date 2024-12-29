import os

RAW_FILES_FOLDER = "raw/"
PARSED_FILES_FOLDER = "parsed/"
replace_num = 0

NAMES = {
    "гг": "mc",
    "автор": "",
    "парень": "undef",
    "какая-то девушка": "undef",
    "владимир": "vladimir",
    "андрей": "andrey",
    "аня": "anya",
    "платон": "platon"
}

BGS = {
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


POST_REPLACES = [
    "vladimir",
    "anya",
    "anya",
    "platon",
    "", ""
]


def parse_raw_file(raw_file):
    parsed_text = ("label start:\n"
                   "$ mc_name = \"Пекус\"\n"
                   "$ vladimir_name = \"Какой-то парень\"\n"
                   "$ platon_name = \"Какой-то парень\"\n"
                   "$ anya_name = \"Какая-то девушка\"\n\n")

    raw_lines = open(RAW_FILES_FOLDER + raw_file, "r", encoding="UTF-8").read().strip().split("\n")
    for line in raw_lines:
        parsed_line = parse_raw_line(line)
        if parsed_line is not None:
            parsed_text += parsed_line + "\n\n"

    return post_parse(parsed_text.strip().replace("\n", "\n    "))


def parse_raw_line(raw_line):
    splitted_line = list(map(lambda x: x.strip(), raw_line.split(":")))

    try:
        command = parse_prefix(splitted_line[0])
        if command in NAMES or len(splitted_line) == 1:
            return parse_char_line(splitted_line)
        elif command == "bg":
            return parse_bg(splitted_line)
        elif command == "sfx":
            return parse_sfx(splitted_line)
        elif command == "m":
            return parse_music(splitted_line)

    except Exception as e:
        return f"show text \"хуйня: \'{raw_line}\'\nerror: {e}\""


def parse_char_line(line):
    global replace_num
    char = None
    if len(line) == 2:
        char = line[0].lower()

    text = line[-1].replace("*имя*", "[mc_name]")

    if char == "автор":
        line = f"\"{text}\""
    elif char is not None:
        name = NAMES[parse_prefix(char)]
        if name == "undef":
            name = "replace" + str(replace_num)
            replace_num += 1

        if parse_suffix(char) == "в мыслях":
            text = "{thoughts}" + text + "{/thoughts}"

        line = str()
        if name!= "mc": line = f"show {name}\n"
        line += f"{name} \"{text}\""

    else:
        line = f"show text \"{text}\" at truecenter with dissolve\npause {2.5 * len(text.split())}\nhide text"

    return line


def parse_bg(line):
    bg = line[1].split()[0].lower()
    return f"scene {BGS[bg]}"


def parse_sfx(line):
    return


def parse_music(line):
    return


def parse_prefix(text):
    return text.lower().split("(")[0].strip()


def parse_suffix(text):
    text = text.lower().split("(")[1].strip()[:-1] if "(" in text else text
    return text


def post_parse(text):
    global replace_num
    for i in range(replace_num):
        text = text.replace(f"replace{i}", POST_REPLACES[i])

    return text


def write_parsed_script(text):
    output = open(PARSED_FILES_FOLDER + file, "w", encoding="UTF-8")
    output.write(text)
    output.close()


for file in os.listdir(RAW_FILES_FOLDER):
    parsed_text = parse_raw_file(file)
    write_parsed_script(parsed_text)
