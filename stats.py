def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    number_of_words(file_contents)

def number_of_words(text):
    word_list = []
    word_list = text.split()
    word_counter = 0
    for word in word_list:
        word_counter += 1
    print(f"Found {word_counter} total words")


def sort_on(item):
    return item["num"]

def count_characters(file_path):
    with open(file_path) as f:
        text = f.read()
        unsorted_characters = {}
        unsorted_list = []
        sorted_list = []

        for character in text:
            if character.isalpha():
                character = character.lower()
                if character not in unsorted_characters:
                    unsorted_characters[character] = 1
                else: 
                    unsorted_characters[character] += 1
        
        for key, value in unsorted_characters.items():
            unsorted_list.append({"char": key, "num": value}) 
        
        unsorted_list.sort(reverse=True, key=sort_on)
        sorted_list = unsorted_list
        
    return sorted_list   

    