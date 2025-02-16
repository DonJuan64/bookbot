def main():
    # Path to the text file
    book_path = "books/frankenstein.txt"

    # Step 1: Read the text from the file
    text = get_book_text(book_path)

    # Step 2: Count and print the total number of words
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    # Step 3: Count the frequency of alphabetic characters
    letter_counts = count_letters(text)

    # Step 4: Print the sorted character counts in a formatted report
    print_character_report(letter_counts)


def get_book_text(path):
    """Reads the content of the file at the given path."""
    with open(path, "r") as f:
        return f.read()


def get_num_words(text):
    """Counts and returns the number of words in the text."""
    words = text.split()
    return len(words)


def count_letters(text):
    """
    Counts the frequency of each alphabetic letter in the text.
    Ignores case and non-alphabetic characters.
    Returns a dictionary with letters as keys and their counts as values.
    """
    char_count = {}  # Start the dictionary
    for char in text:
        char = char.lower()  # Convert to lowercase for case-insensitivity
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def print_character_report(letter_counts):
    """
    Prints a sorted text report of letter frequencies.
    """
    print("\nCharacter frequencies:")
    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

    for letter, count in sorted_counts:
        print(f"The '{letter}' character was found {count} times")


# Run the main function
main()

