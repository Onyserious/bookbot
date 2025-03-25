def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    words_dic = {}
    lowercase = text.lower()

    for i in lowercase:
        if i in words_dic:
            words_dic[i] += 1
        else:
            words_dic[i] = 1
    return words_dic

def sort_on(dict):
    return dict["count"]

def sort_char_count(char_counts_dict):
    char_list = []

    for char, count in char_counts_dict.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

