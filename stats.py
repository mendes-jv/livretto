def get_num_words(file_content):
    try:
        return len(file_content.split())
    except Exception as e:
        raise Exception(f"Error counting words: {str(e)}")
