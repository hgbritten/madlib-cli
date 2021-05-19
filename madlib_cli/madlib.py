# print("Welcome to the madlib game")
# input("> ")


def read_template(path):
    with open(path) as text:
        return text.read().strip()


# {a}
def parse_template(template):
    final_stripped_template = ""
    collecion_of_parts = []
    current_part = ""
    capturing_part = False
    for char in template:
        if char == "{":
            final_stripped_template += char
            capturing_part = True
            current_part = ""
        if char == "}":
            final_stripped_template += char
            capturing_part = False
            collecion_of_parts.append(current_part)
        if capturing_part:
            current_part += char
        return final_stripped_template, tuple(collecion_of_parts)


def merge():
    pass
