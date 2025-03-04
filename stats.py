def get_book_text(path):
    with open(path) as f:
                   file_contents = f.read()
                   return file_contents

def words_count():
        book_text = get_book_text("books/frankenstein.txt")
        words = len(book_text.split())
        print ("Found", words, "total words")

def character_count(book_text):
        lowercase_characters = book_text.lower()
        char_count = {}
        for char in lowercase_characters:
            if char in char_count:
                    char_count[char] += 1
            else:
                    char_count[char] = 1
        return char_count

def sorted_list(char_count):
        chars_list = []
        for char, count in char_count.items():
                char_dict = {"char": char, "count": count}
                chars_list.append(char_dict)
        
        def sort_on(char_dict):
                return char_dict["count"]
        chars_list.sort(reverse=True, key=sort_on)
        return chars_list