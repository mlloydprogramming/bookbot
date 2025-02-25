from stats import word_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path to book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    lower_text = text.lower()
    num_words = word_count(text)
    letter_count = {}
    for letter in lower_text:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    print(f"{num_words} words in the document")
    for item in letter_count:
        if item.isalpha():
            print(f"{item}: {letter_count[item]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()