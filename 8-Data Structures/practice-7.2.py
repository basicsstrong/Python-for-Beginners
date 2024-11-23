def get_unique_words(words_list):
    """
    Takes a list of words and returns a set of unique words.
    
    Args:
        words_list (list): A list of words (strings).
    
    Returns:
        set: A set of unique words.
    """
    # Convert the list to a set to remove duplicates
    unique_words = set(words_list)
    return unique_words

# Example usage
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "apple", "banana", "date"]
    unique_words = get_unique_words(words)
    print("Original List:", words)
    print("Unique Words:", unique_words)
