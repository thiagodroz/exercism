def is_pangram(sentence):
    sentence = sentence.lower()

    for letter in "abcdefghijklmnopqrstuvwxyz":
        if not letter in sentence:
            return False

    return True
