from stats import get_num_words, count_letters, sort_char_count
import sys

def print_report(book_path,num_words,sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts_dict = count_letters(text)
    sorted_chars = sort_char_count(char_counts_dict)
    print_report(book_path,num_words,sorted_chars)
    return 

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
