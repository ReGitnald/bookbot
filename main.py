import re
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    char_dict = {}
    for character in text.lower():
        if character in char_dict:
            char_dict[character] +=1
        else:
            char_dict[character] =1
    return char_dict

def book_report(book_path, text):
    headline = f"Report of{book_path}"
    report = headline + f"\n{get_num_words(text)} words found in the document\n"
    cdict = get_character_count(text)
    sortc = sorted(cdict,reverse=True, key=cdict.__getitem__)
    # print(sortc)
    for char in sortc:
        if char.isalpha():
            line = f"\nThe {char} character was found {cdict[char]} times"
            report = report+ line
    return report

# main()
book_path = "books/frankenstein.txt"
text = get_book_text(book_path)
print(book_report(book_path, text))
