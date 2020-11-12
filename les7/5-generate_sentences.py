def generate_sentences(worddict, sentence_format):
    worddict = change_to_list(worddict)

    for wordspace in sentence_format:
        pass

    sentences = []

    return sentences


def change_to_list(worddict):
    newdict = dict()
    for word, type in worddict.items():
        if type in newdict:
            newdict[type].append(word)
        else:
            newdict[type] = [word]

    return newdict
