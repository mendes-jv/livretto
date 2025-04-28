def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    try:
        book_text = get_book_text("books/frankenstein.txt")
        print(book_text)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
