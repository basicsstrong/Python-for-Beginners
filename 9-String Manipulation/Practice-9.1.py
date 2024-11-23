def format_sentence(sentence):
    """
    Takes a sentence, removes leading and trailing spaces, 
    and returns the sentence in uppercase.
    
    Args:
        sentence (str): The input sentence (string).
    
    Returns:
        str: The formatted sentence in uppercase without leading or trailing spaces.
    """
    # Remove leading and trailing spaces and convert to uppercase
    formatted_sentence = sentence.strip().upper()
    return formatted_sentence

# Example usage
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = format_sentence(sentence)
    print("Formatted Sentence:", result)
