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

def count_characters(file_path):
    with open(file_path) as f:
        text = f.read()
        character_count = {}
        for character in text:
            lower_character = character.lower()
            if lower_character not in character_count:
                character_count[lower_character] = 1
            else: 
                character_count[lower_character] += 1
    sorted_list = []
    sorted_list = sorted(character_count.items(), key=lambda pair: pair[1], reverse=True)
    character_count = dict(sorted_list)
    return character_count