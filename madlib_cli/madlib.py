# print("Welcome to the madlib game")
# input("> ")


def read_template(path):
    with open(path) as text:
        return text.read().strip()


# {a}
def parse_template(template):
    final_stripped_template = ""
    collection_of_parts = []
    current_part = ""
    capturing_part = False
    for char in template:
        if char == "{":
            final_stripped_template += char
            capturing_part = True
            current_part = ""
        elif char == "}":
            final_stripped_template += char
            capturing_part = False
            collection_of_parts.append(current_part)
        elif capturing_part:
            current_part += char
        else:
            final_stripped_template += char

    # This returns a Tuple. It knows this because of the comma
    return_value = final_stripped_template, tuple(collection_of_parts)
    return return_value
    # return final_stripped_template, tuple(collection_of_parts)


def merge(template, parts):
    merged = template.format(*parts)
    return merged


if __name__ == "__main__":
    print(
        """

  *****************************************************

  Welcome. We are going to play Madlibs!
  You will be prompted with a series of prompts.
  Provide appropriate responses to complete the Madlib

  *****************************************************

  """
    )

    def get_responses(speech_parts):
        # need template text to put words into
        user_responses = []
        for part in speech_parts:
            prompt = f"Provide a/an {part} "
            response = input(prompt)
            user_responses.append(response)

        return user_responses

    stripped_template, speech_parts = parse_template(
        read_template("assets/dark_and_stormy_night.txt")
    )

    responses = get_responses(speech_parts)
    print(merge(stripped_template, responses))
    # Want to loop through words to set prompt for input
