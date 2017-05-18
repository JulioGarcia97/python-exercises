def word_count(string):
    word_dict = string.lower()
    new_dict = {}
    for word in word_dict.split():
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    print(new_dict)
    
word_count("I really love to learn python, I try too understand all concepts")