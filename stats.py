def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def get_word_count(file):
    return len(file.split())
def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count