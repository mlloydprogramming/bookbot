def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower_text = text.lower()
    num_words = word_count(text)
    letter_count = {}
    for letter in lower_text:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    print(f"{num_words} words in the document")
    for item in letter_count:
        if item.isalpha():
            print(f"The '{item}' character was found {letter_count[item]} times")

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()