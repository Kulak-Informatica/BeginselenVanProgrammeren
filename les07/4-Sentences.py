def all_sentences(wordlst):
    if len(wordlst) <= 1:
        return wordlst

    sentence_lst = []
    for word in wordlst:
        temp_wordlst = list(wordlst)
        temp_wordlst.remove(word)
        # We need to add this word to every string in list of sentences without that word
        # That's the recursive bit: we ask the list of sentences without that word, and add this word to it,
        # for every word in the given wordlist
        sentences = all_sentences(temp_wordlst)
        for sentence in sentences:
            sentence = word + " " + sentence
            sentence_lst.append(sentence)

    return sentence_lst


def main():
    wordlst = ["Hey", "hoi", "hallo", "Dimmeboy"]
    print(all_sentences(wordlst))


main()
