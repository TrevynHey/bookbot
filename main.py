def main(path_to_file):
    with open(path_to_file) as f:
        book_text = get_book_text(path_to_file)
        num_words = get_num_words(book_text)
        letter_dict = character_count(book_text)
        print_report(path_to_file,num_words, letter_dict)

def get_book_text(book_loc):
    with open(book_loc) as f:
        return f.read()

def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def character_count(text):
    letter_dict = {}
    for letter in text:
        #print(letter)
        if letter.lower() in letter_dict:
            letter_dict[letter.lower()] += 1
        else:
            letter_dict[letter.lower()] = 1
    #print(letter_dict)
    return letter_dict

def print_report(book_loc,num_words, letter_dict):
    print(f"--- Begin reporting of {book_loc} ---")
    print(f"{num_words} words found in the document")
    print("")
    for key in letter_dict:
        print(f"The '{key} character was found {letter_dict[key]} times")
    print("--- End report ---")

book_loc = "books/frankenstein.txt"
main(book_loc)