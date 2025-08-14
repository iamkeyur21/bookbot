def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_counts(char_count):
    char_list = []
    for char, num in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list