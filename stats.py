def get_num_words(file_content):
    try:
        return len(file_content.split())
    except Exception as e:
        raise Exception(f"Error counting words: {str(e)}")


def get_num_chars_occurrence(file_content):
    try:
        char_occurrence = {}
        for char in file_content.lower():
            if char in char_occurrence:
                char_occurrence[char] += 1
            else:
                char_occurrence[char] = 1
        return char_occurrence
    except Exception as e:
        raise Exception(f"Error counting characters: {str(e)}")
