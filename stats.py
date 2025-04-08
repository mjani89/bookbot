def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_num_chars(text):
    word_dict = {}
    for char in text:
        char = char.lower()
        if char not in word_dict:
            word_dict[char] = 1
        else:
            word_dict[char] += 1
    return word_dict

def sort_on(sorted_dict):
    for char in sorted_dict:
        if char.isalpha():
            print(f"{char}: {sorted_dict[char]}")
    return None