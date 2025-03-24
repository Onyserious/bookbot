from stats import get_num_words, count_letters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    count = count_letters(text)
    print(count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
