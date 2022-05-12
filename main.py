

# S > NP VP
# VP > V NP PP , VP PP
# PP > P NP
# V > "saw" , "ate" , "walked"
# NP > "John" , "Mary" , "Bob" , Det N PP , Det N
# Det > "a" , "an" , "the" , "my"
# N > "man" , "dog" , "cat" , "telescope" , "park"
# P > "in" , "on" , "by" , "with"

def parse_sentence(sentence, main_dict):
    sentence = sentence.split()
    print(sentence)
    sentence_keys = []
    for word in sentence:
        word = word.lower()
        word_key = ''
        for key1, value1 in main_dict.items():
            # print(key, value)
            for key2, value2 in value1.items():
                # print(key2, value2)
                value2 = [x.lower() for x in value2]
                if word in value2:
                    word_key = key2
        sentence_keys.append(word_key)
    print(sentence_keys)





def main(filename, sentence):
    main_dict = {'WORDS':{"P": ['in', 'on', 'by', 'with'], 'N': ['man', 'dog', 'cat', 'telescope', 'park'], 'Det': ['a', 'an', 'the', 'my'], "NP": ['John', 'Mary', 'Bob'], 'V': ['saw', 'ate', 'walked']}, 'DATA':{'NP': [['Det', 'N', 'PP'], ['Det', 'N']], 'PP': ['P', 'NP'], 'VP': [['V', 'NP', 'PP'], ['VP', 'PP']], 'S': ['NP', 'VP']}}

    parse_sentence(sentence, main_dict)

main('grammer.txt', 'Bob saw a dog in the park')
