def get_word(prompt):
    return input(prompt + " ")


def main():
    print("Welcome to the Mad Libs game!")

    # Collecting words from the user
    adjective1 = get_word("Enter an adjective")
    noun1 = get_word("Enter a noun")
    verb1 = get_word("Enter a verb")
    adverb1 = get_word("Enter an adverb")
    noun2 = get_word("Enter another noun")

    # Template for the story
    story = f"""
    Once upon a time, in a {adjective1} land, there was a {noun1} who loved to {verb1} {adverb1}.
    Every day, the {noun1} would visit the {noun2} and they would have amazing adventures together.
    It was a truly {adjective1} time for everyone involved!
    """

    print("\nHere's your Mad Libs story:")
    print(story)


if __name__ == "__main__":
    main()
