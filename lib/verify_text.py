def verify_text(text):
    suitable_punct_marks = "!?."
    
    if text == "":
        raise Exception("No text")
    elif text[0].isupper() and text[-1] in suitable_punct_marks:
        return "This text is CORRECT!"
    elif text[0].islower():
        if any(char in suitable_punct_marks for char in text):
            return "No capital letter at the start of the sentence"
        else:
            return "No capital letter at start or punctuation at the end"
    else:
        raise Exception("No punctuation finishing the sentence")

    
    












