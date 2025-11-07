def count_words(text):
    return len(text.split())

def get_char_counts(text):
    chars = {}
    for ch in text:
        ch = ch.lower()
        chars[ch] = chars.get(ch, 0) + 1
    return chars

def sort_on(d):
    return d["num"]

def sort_char_counts(char_counts):
    items = []
    for ch, n in char_counts.items():
        items.append({"char": ch, "num": n})
    items.sort(key=sort_on, reverse=True)  # in-place, greatest → least
    return items
