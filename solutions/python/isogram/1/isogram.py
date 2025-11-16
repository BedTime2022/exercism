def is_isogram(string):
    lowered = [c.lower() for c in string if c.isalpha()]
    return len(set(lowered)) == len(lowered)
