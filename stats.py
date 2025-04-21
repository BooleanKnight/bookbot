def count_words(text):
    words = text.split()
    return len(words)

def return_characters(text):
    char_counts = {}
    for t in text:
        t = t.lower()
        if t in char_counts:
            char_counts[t] += 1
        else:
            char_counts[t] =1
    return char_counts


def dictionary_sort(dict):
    return_value = []
    for d,i in dict.items():
        item = {"character": d, "count": i}
        return_value.append(item)
    return_value.sort(key=lambda item: item["count"], reverse=True)
    return return_value





