from stats import get_book_text, count_characters
import sys

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_book_text(sys.argv[1])
    print("--------- Character Count -------")
    dictionary = count_characters(sys.argv[1])
    for item in dictionary:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")
    

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print(sys.argv)