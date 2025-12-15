from stats import get_book_text, count_characters


def main():
    get_book_text("books/frankenstein.txt")


    dictionary = {}
    dictionary = count_characters("books/frankenstein.txt")
    print(dictionary)

main()