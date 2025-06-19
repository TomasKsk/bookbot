from stats import (
    get_num_words, 
    get_chars_dict, 
    sort_num_dict
)

import sys

def main():
    arguments = sys.argv
    if len(arguments) == 2:
        book_path = arguments[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        all_chars = get_chars_dict(text)
        sort_chars = sort_num_dict(all_chars)
        print_report(book_path, num_words, sort_chars)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()


