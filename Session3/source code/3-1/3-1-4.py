def word_printer():
    status = True
    word_set = ''
    while status:
        words = input()
        if words == 'END':
            status = False
        else:
            for word in words.split():
                if word not in word_set:
                    word_set = word_set + ' ' + word
            print(word_set)   

print(word_printer())