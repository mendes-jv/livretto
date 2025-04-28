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


def sort_by_occurrence(occurrence):
    try:
        return [
            {"char": char, "num": count}
            for char, count in sorted(occurrence.items(),
                                      key=lambda x: x[1],
                                      reverse=True)
        ]
    except Exception as e:
        raise Exception(f"Error sorting characters occurrence: {str(e)}")
