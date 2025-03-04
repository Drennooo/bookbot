import sys
if (len(sys.argv)) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]
    print(f"Processing file: {path}")
    with open(path, "r") as book_file:
        content = book_file.read()  # Read the whole content of the file
        print("File successfully read!")  # Just a little feedback for the user
from stats import get_book_text, words_count, character_count, sorted_list

def main():
    # Get the path to the book
    path = sys.argv[1]
    
    # Get the book text
    book_text = get_book_text(path)
    
    # Print the report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    words_count()  # This function prints the word count itself
    
    # Get character counts and sort them
    chars = character_count(book_text)
    sorted_chars = sorted_list(chars)
    
    # Print character count section
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    # Print the report footer
    print("============= END ===============")

if __name__ == "__main__":
    main()