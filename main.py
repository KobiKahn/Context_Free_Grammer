

# S > NP VP
# VP > V NP PP , VP PP
# PP > P NP
# V > "saw" , "ate" , "walked"
# NP > "John" , "Mary" , "Bob" , Det N PP , Det N
# Det > "a" , "an" , "the" , "my"
# N > "man" , "dog" , "cat" , "telescope" , "park"
# P > "in" , "on" , "by" , "with"

def make_dictionary(filename):
    main_dict = {'WORDS': {}, 'DATA': {}}
    mini_dict = {}
    word_dict = {}
    data_dict = {}

    with open(filename) as file:
        for row in file:
            word_list = []
            data_list = []
            x = 0
            row = row.split()
            row_len = len(row)
            for word in row:
                x += 1
                if x > 2:
                    if word[0] == '"':
                        # print(word)
                        word_list.append(word)
                    elif word != '|':
                        data_list.append(word)

            word_dict[row[0]] = word_list
            data_dict[row[0]] = data_list

    main_dict['WORDS'] = word_dict
    main_dict['DATA'] = data_dict
    print(main_dict)

def parse_sentence(sentence, main_dict):
    sentence = sentence.split()
    word_tuple_list = []
    # print(sentence)
    sentence_keys = []
    for word in sentence:
        word = word.lower()
        word_key = ''
        for key1, value1 in main_dict.items():
            # print(key, value)
            for key2, value2 in value1.items():
                # print(key2, value2)
                if key1 == 'WORDS':
                    for i in range(len(value2)):
                        value2[i] = value2[i].lower()
                        # print(value2[i])

                if word in value2:
                    word_key = key2
        sentence_keys.append(word_key)
        word_tuple_list.append((word, word_key))

    for word in word_tuple_list:
        print(word)



def main(filename, sentence):
    main_dict = {'WORDS':{"P": ['in', 'on', 'by', 'with'], 'N': ['man', 'dog', 'cat', 'telescope', 'park'], 'Det': ['a', 'an', 'the', 'my'], "NP": ['John', 'Mary', 'Bob'], 'V': ['saw', 'ate', 'walked']}, 'DATA':{'NP': [['Det', 'N', 'PP'], ['Det', 'N']], 'PP': ['P', 'NP'], 'VP': [['V', 'NP', 'PP'], ['VP', 'PP']], 'S': ['NP', 'VP']}}
    # print(main_dict)
    main_dict = make_dictionary(filename)
    # parse_sentence(sentence, main_dict)

main('grammer.txt', 'The telescope saw a dog in the park with a cat')
