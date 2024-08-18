def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    char_counts = count_characters(text)
    sorted_char_counts = sort_char_counts(char_counts)
    
    print("\nCharacter Counts:")
    for char_info in sorted_char_counts:
        char, count = char_info['char'], char_info['count']
        print(f"The '{char}' character was found {count} times")

    print(f"--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
    
def sort_char_counts(char_counts):
    char_info_list = [{'char': char, 'count': count} for char, count in char_counts.items()]
    char_info_list.sort(reverse=True, key=lambda x: x['count'])
    return char_info_list

main()