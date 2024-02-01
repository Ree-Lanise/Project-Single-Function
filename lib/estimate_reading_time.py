def estimate_reading_time(text):
    split_words = text.split()
    word_count = len(split_words)
    if text == "":
        raise Exception("Text needs to be added in order to calculate a reading time")
    return word_count / 200
