import os


class ScriptParser:
    RAW_FILES_FOLDER = "raw/"
    PARSED_FILES_FOLDER = "parsed/"

    ACT1_START_STRING = ("label start:\n"
                         "$ mc_name = \"Пекус\"\n"
                         "$ vladimir_name = \"Какой-то парень\"\n"
                         "$ platon_name = \"Какой-то парень\"\n"
                         "$ anya_name = \"Какая-то девушка\"\n\n")

    NAMES = {
        "ГГ": "mc",
        "ГГ (В мыслях)": "mc",
        "ГГ (в мыслях)": "mc",
        "Автор": "",
        "Какой-то парень": "undef",
        "Какая-то девушка": "undef",
        "Владимир": "vladimir",
        "Андрей": "andrey",
        "Аня": "anya",
        "Платон": "platon"
    }

    BGS = {
        "black": "black",
        "gukoutside": "guk_outside",
        "rtfoutside": "rtf_outside",
        "collegetown": "collegetown",
        "dormitorycorridor": "dormitory_corridor",
        "room": "dormitory_room",
        "trainstation": "railway_station",
        "phone1": "phone1",
        "phone2": "phone2",
        "phone": "phone",
        "mirror": "mirror"
    }

    def __init__(self):
        self.replace_index = 0

    def parse_script(self):
        for file in os.listdir(self.RAW_FILES_FOLDER):
            self.parse_file(file)

    def parse_file(self, file):
        raw_text = open(self.RAW_FILES_FOLDER + file, "r", encoding="UTF-8").read().strip()
        raw_lines = raw_text.split("\n")

        parsed_text = self.parse_lines(raw_lines)

        if "act1" in file:
            parsed_text = self.ACT1_START_STRING + parsed_text

        self.write_parsed_file(file, parsed_text)

    def parse_lines(self, lines):
        parsed_lines = []

        for line in lines:
            if line is None or line.startswith("Сцена"):
                continue

            splitted_line = list(map(lambda x: x.strip(), line.split(":")))

            if len(splitted_line) == 1 or splitted_line[0] in self.NAMES:
                parsed_lines.append(self.parse_char_line(splitted_line))
            elif splitted_line[0] == "BG":
                parsed_lines.append(self.parse_bg(splitted_line[1]))
            elif splitted_line[0] == "C":
                parsed_lines.append(self.parse_char_show(splitted_line[1]))
            else:
                continue

            parsed_lines.append("")

        return "\n".join(parsed_lines).replace("\n", "\n    ")

    def write_parsed_file(self, file, text):
        output = open(self.PARSED_FILES_FOLDER + file, "w", encoding="UTF-8")
        output.write(text)
        output.close()

    def parse_char_show(self, line):
        name = str()
        for n in self.NAMES.values():
            if len(n) > 1 and line.lower().startswith(n):
                name = n
                break

        face = line[len(name)::].lower()
        if len(face) <= 1:
            face = "base"

        return f"show {name}_{face}\nhide {name}_{face}"

    def parse_char_line(self, line):
        text = line[-1].replace("*имя персонажа*", "[mc_name]").replace("*имя*", "[mc_name]")

        if len(line) == 1:
            return f"show text \"{text}\" at truecenter with dissolve\npause {0.5 * len(text.split())}\nhide text"
        elif line[0] == "Автор":
            return f"\"{text}\""
        else:
            name = self.NAMES[line[0]]

            if name == "undef":
                name = "replace" + str(self.replace_index)
                self.replace_index += 1

            if "в мыслях" in line[0].lower():
                text = "{thoughts}" + text + "{/thoughts}"

            return f"{name} \"{text}\""

    def parse_bg(self, line):
        bg = line.lower()

        if bg not in self.BGS:
            bg_string = "black"
        else:
            bg_string = self.BGS[bg]

        return f"scene {bg_string}"


if __name__ == "__main__":
    parser = ScriptParser()
    parser.parse_script()
