from stats import word_count, character_counts, sorted_dictionary
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# storing contents of text file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
              
        return file_contents  
    
word_counts = word_count(get_book_text(sys.argv[1]))
character__dict = character_counts(get_book_text(sys.argv[1]))
dictionary_list = sorted_dictionary(character__dict)
    
def main():
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {sys.argv[1]}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {word_counts} total words\n")
    print("--------- Character Count -------\n")
    for dict in dictionary_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}\n")
    print("============= END ===============")
    
main()