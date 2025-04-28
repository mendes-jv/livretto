from stats import get_num_words


def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    try:
        book_text = get_book_text("books/frankenstein.txt")
        num_words = get_num_words(book_text)
        print(f"{num_words} words found in the document")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
