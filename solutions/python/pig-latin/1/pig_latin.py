def translate(text):
    vowels = ("a", "e", "i", "o", "u")
    results = []
    
    for word in text.split():
        if word.startswith(vowels + ("xr", "yt")):
            results.append(word + "ay")
            continue

        for i, ch in enumerate(word):
            if ch in vowels or (ch == "y" and i != 0):
                if word[i-1:i+1] == "qu":
                    i += 1
                results.append(word[i:] + word[:i] + "ay")
                break

    return " ".join(results)
