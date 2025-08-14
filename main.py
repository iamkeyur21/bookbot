def main():
    from stats import get_book_text, get_word_count, get_char_count
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")
    char_counts = get_char_count(book_text)
    print(char_counts)

main()