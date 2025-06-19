from stats import word_count, character_counts

rel_filepath = "./books/frankenstein.txt"

# storing contents of text file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
              
        return file_contents  
    
word_counts = word_count(get_book_text(rel_filepath))
character__dict = character_counts(get_book_text(rel_filepath))  
    
def main():
    print(f"{word_counts} words found in the document")
    print(character__dict)
    
main()