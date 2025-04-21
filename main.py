
import sys
from stats import count_words, return_characters, dictionary_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    import sys

    # Check for correct command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1
    
    # Safely retrieve the file path from sys.argv[1]
    bookpath = sys.argv[1]

    # Attempt to open the file and read the text
    try:
        with open(bookpath, "r") as file:
            text = file.read()  # Read file contents into "text"
    except FileNotFoundError:
        print(f"Error: The file '{bookpath}' does not exist.")
        sys.exit(1)

    # Proceed with book analysis after the file is successfully read
    print("File has been read successfully!")

    # Count words in the text
    word_count = count_words(text)
    print(f"Found {word_count} total words.")

    # Count characters in the text
    character_count = return_characters(text)

    # Sort and display the character counts
    sort_dictionary = dictionary_sort(character_count)

    print("--------- Character Count -------")
    for item in sort_dictionary:
        char = item["character"]
        count = item["count"]

        # Display only alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")


if __name__ == "__main__":
    main()





if __name__ == "__main__":
    main()





