from sys import argv

from stats import get_num_chars_occurrence
from stats import get_num_words
from stats import sort_by_occurrence


def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    try:
        if len(argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            exit(1)
        book_text = get_book_text(argv[1])
        num_words = get_num_words(book_text)
        char_occurrence = get_num_chars_occurrence(book_text)
        sorted_occurrence = sort_by_occurrence(char_occurrence)
        print("============ BOOKBOT ============\n"
              f"Analyzing book found at {argv[1]}...\n"
              "----------- Word Count ----------\n"
              f"Found {num_words} total words\n"
              "----------- Character Count ----------")
        for dict in sorted_occurrence:
            if dict["char"].isalpha():
                print(f"{dict['char']}: {dict['num']}")
        print("============= END ===============")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
