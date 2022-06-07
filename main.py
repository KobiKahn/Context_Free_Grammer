# S > NP VP
import string


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
    punctuation = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~”“'
    with open(filename) as file:
        for row in file:
            word_list = []
            data_list2 = []
            data_string = ''
            data_list = []
            x = 0
            row = row.split()
            row_len = len(row)
            for word in row:
                x += 1
                if x > 2:
                    if word[0] == '"':
                        # print(word)
                        word = word.translate(str.maketrans("", "", punctuation))
                        word_list.append(word)
                    elif word == '|':
                        data_list.append(',')
                    elif word != '|':
                        data_list.append(word)
            # print(data_list)
            for word in data_list:
                data_string += word + ' '
            for val in data_string.split(','):
                if val == '' or val == ' ':
                    pass
                else:
                    data_list2.append(val)

            word_dict[row[0]] = word_list
            data_dict[row[0]] = data_list2

    main_dict['WORDS'] = word_dict
    main_dict['DATA'] = data_dict
    return main_dict


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

    return word_tuple_list


def get_order(main_dict):
    new_list = []
    for val in main_dict['DATA']:
        if main_dict['DATA'][val]:
            new_list.insert(0, val)
    return new_list


def check_sentence(tuple_list, m_dict, order_list):
    new_tuple_list = []
    order_list_counter = -1
    for numb in range(len(order_list)):  # loops through order list len to reach all possible combos
        order_list_counter += 1  # updates orderlistcounter for indexing
        requirements = m_dict['DATA'][order_list[order_list_counter]]  # gets proper set of reqs for val
        counter_req = 0
        for req in requirements:  # loops through the different order combos
            req_list = [val for val in req.split() if val != '']  # makes the req list only the needed combos
            counter_tuple = -1
            print(tuple_list)
            print(req_list)
            if counter_req >= len(req_list) - 1:
                counter_req = 0
            else:
                for num in range(len(tuple_list)):
                    counter_tuple += 1
                    if counter_tuple >= len(tuple_list):
                        pass
                    elif req_list[counter_req] == tuple_list[counter_tuple][-1] and counter_tuple+1 < len(tuple_list) and counter_req+1 < len(req_list):
                        if req_list[counter_req + 1] == tuple_list[counter_tuple + 1][-1]:
                            # print(tuple_list[counter_tuple], tuple_list[counter_tuple + 1])
                            if len(req_list) > 2 and counter_tuple+2 < len(tuple_list) and counter_req+2 < len(req_list):
                                if req_list[counter_req + 2] == tuple_list[counter_tuple + 2][-1]:
                                    new_tuple_list.append((
                                        tuple_list[counter_tuple][0] + ' ' + tuple_list[counter_tuple + 1][0]
                                        + ' ' + tuple_list[counter_tuple + 2][0],
                                        order_list[order_list_counter]))
                                    counter_tuple += 2
                            else:
                                # print(req_list)
                                new_tuple_list.append(
                                    (tuple_list[counter_tuple][0] + ' ' + tuple_list[counter_tuple + 1][0],
                                     order_list[order_list_counter]))
                                counter_tuple += 1
                    else:
                        new_tuple_list.append(tuple_list[counter_tuple])
                tuple_list = new_tuple_list
                # print(tuple_list)
                new_tuple_list = []
        counter_req += 1
    print(tuple_list)


def main(filename, sentence):
    # main_dict = {'WORDS': {"P": ['in', 'on', 'by', 'with'], 'N': ['man', 'dog', 'cat', 'telescope', 'park'],
    #                        'Det': ['a', 'an', 'the', 'my'], "NP": ['John', 'Mary', 'Bob'],
    #                        'V': ['saw', 'ate', 'walked']},
    #              'DATA': {'NP': [['Det', 'N', 'PP'], ['Det', 'N']], 'PP': ['P', 'NP'],
    #                       'VP': [['V', 'NP', 'PP'], ['VP', 'PP']], 'S': ['NP', 'VP']}}
    # main_dict = {'WORDS':{"P": ['in', 'on', 'by', 'with'], 'N': ['man', 'dog', 'cat', 'telescope', 'park'], 'Det': ['a', 'an', 'the', 'my'], "NP": ['John', 'Mary', 'Bob'], 'V': ['saw', 'ate', 'walked']}, 'DATA':{'NP': [['Det', 'N', 'PP'], ['Det', 'N']], 'PP': ['P', 'NP'], 'VP': [['V', 'NP', 'PP'], ['VP', 'PP']], 'S': ['NP', 'VP']}}

    main_dict = make_dictionary(filename)
    order_list = get_order(main_dict)
    n_sentence = parse_sentence(sentence, main_dict)
    check_sentence(n_sentence, main_dict, order_list)


# Bob saw a dog in the park
# The telescope saw a dog in the park with a cat
# the telescope ate the cat
# john saw mary in the park
# bob walked a dog in the park
# the dog saw a cat
# a cat with a dog saw john
main('grammer.txt', 'The telescope saw a dog in the park with a cat')
