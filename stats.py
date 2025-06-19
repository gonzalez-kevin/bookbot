def word_count(book_text):
    words = book_text.split()
    return len(words)

def character_counts(book_text):
    char_dict = {}
    
    # convert book text to lowercase outside of for loop 
    lc_text = book_text.lower()
    # loop to add characters to the dictionary
    for char in lc_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
            
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_dictionary(dict):
    # create list of dicts splitting the key, value pairs in the original dict
    list_of_dicts = [{"char": key, "num": value} for key, value in dict.items()]
    # sort list based on num value greatest to least
    list_of_dicts.sort(reverse = True, key = sort_on)
    return list_of_dicts