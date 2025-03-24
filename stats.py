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

