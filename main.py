from stats import get_num_words
from stats import get_num_chars
from stats import sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        filepath = sys.argv[1]
        print(f"Analyzing book found at {filepath}")
        book = get_book_text(filepath)
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book)} total words")
        print("----------- Character Count ----------")
        book_dict = get_num_chars(book)
        sorted_book_dict= dict(sorted(book_dict.items(),key=lambda item: item[1], reverse=True))
        sort_on(sorted_book_dict)
        print("============= END ===============")


main()