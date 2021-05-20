from madlib_cli.madlib import read_template, parse_template, merge

print(
    """

*****************************************************

Welcome. We are going to play Madlibs!
You will be prompted with a series of prompts.
Provide appropriate responses to complete the Madlib

*****************************************************

"""
)


user_responses = []


def get_responses():
    adj1 = input("Provide an Adjective")
    user_responses.append(adj1)
    adj2 = input("Provide an Adjective")
    user_responses.append(adj2)
    noun = input("Provide a Noun")
    user_responses.append(noun)


madlib = read_template("dark_and_stormy_night.txt")
parsed_text, adjectives = parse_template(madlib)
parts = get_responses()
print(user_responses)
print(merge(parsed_text, user_responses))
