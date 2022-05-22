import codecs

with codecs.open("final_stopwords.txt", encoding='utf-8') as f:
 
    stop_words = f.read()
    stop_words_list = stop_words.split()



def stop_words_removal(sentence):
    for i in sentence:
        if i in stop_words_list:
            print(i)
            sentence.remove(i)
    return sentence


