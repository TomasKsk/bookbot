def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def sort_num_dict(dict):
    items = dict.items()
    # [k for k in items] - python comprehension to create lists in one line
    key_value_pairs = [{"char": key, "num": value} for key, value in items]
    return sorted(key_value_pairs, reverse=True, key=sort_on)
