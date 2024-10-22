def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_list = dictionary_to_list(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_num_chars(text):
    char_lower = text.lower()
    letter_count = {}
    for char in char_lower:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def sort_on(dictionary):
    return dictionary["num"]

def dictionary_to_list(num_chars_dict):
    sorted_list = []
    for character in num_chars_dict:
        sorted_list.append({"char": character, "num": num_chars_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
 
main()