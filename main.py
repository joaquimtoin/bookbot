from stats import get_book_words
from stats import get_book_chars
from stats import list_of_dictionary
import sys

                      
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    words = get_book_words(path_to_book)
    characters = get_book_chars(path_to_book)
    list_of_characters = list_of_dictionary(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")        
    for i in range(0, len(list_of_characters)):
        line = list_of_characters[i]
        print(f"{line["char"]}: {line["num"]}")
    print("============= END ===============")
       
main()