def is_pangram(sentence):
    sentence = sentence.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    found = set()

    for char in sentence:
        if char in letters:
            found.add(char)

    if len(found) == 26:
        return True
    else:
        return False
