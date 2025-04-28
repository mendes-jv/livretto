from stats import get_num_chars_occurrence
from stats import get_num_words
from stats import sort_by_occurrence


def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    try:
        book_text = get_book_text("books/frankenstein.txt")
        num_words = get_num_words(book_text)
        char_occurrence = get_num_chars_occurrence(book_text)
        sorted_occurrence = sort_by_occurrence(char_occurrence)
        print("============ BOOKBOT ============\n"
              "Analyzing book found at books/frankenstein.txt...\n"
              "----------- Word Count ----------\n"
              f"Found {num_words} total words"
              "----------- Character Count ----------\n"
              f"{sorted_occurrence}\n"
              "============= END ===============")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
