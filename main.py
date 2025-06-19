from stats import word_count, character_counts, sorted_dictionary

rel_filepath = "books/frankenstein.txt"

# storing contents of text file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
              
        return file_contents  
    
word_counts = word_count(get_book_text(rel_filepath))
character__dict = character_counts(get_book_text(rel_filepath))
dictionary_list = sorted_dictionary(character__dict)
    
def main():
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {rel_filepath}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {word_counts} total words\n")
    print("--------- Character Count -------\n")
    for dict in dictionary_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}\n")
    print("============= END ===============")
    
main()