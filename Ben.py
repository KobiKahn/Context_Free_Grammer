

# S > NP VP
# VP > V NP PP , VP PP
# PP > P NP
# V > "saw" , "ate" , "walked"
# NP > "John" , "Mary" , "Bob" , Det N PP , Det N
# Det > "a" , "an" , "the" , "my"
# N > "man" , "dog" , "cat" , "telescope" , "park"
# P > "in" , "on" , "by" , "with"

def parse_sentence(sentence, main_list):
    sentence = sentence.split()

    for word in sentence:
        for dict in main_list:
            for list in dict.values():
                if len(list) > 1:
                    print(list)
                    # for item in list[0]:
                    #     if word.lower() == item.lower():
                    #         print(word)


def main(filename, sentence):
    main_list = [{"P": ['in', 'on', 'by', 'with']}, {'N': ['man', 'dog', 'cat', 'telescope', 'park']}, {'Det': ['a', 'an', 'the', 'my']}, {"NP": [ ['John', 'Mary', 'Bib'], [['Det', 'N', 'PP'], ['Det', 'N']] ]}, {'V': ['saw', 'ate', 'walked']}, {'PP': [[], ['P', 'NP']]}, {'VP': [[], [['V', 'NP', 'PP'], ['VP', 'PP']]]}, {'S': [[], ['NP', 'VP']]}]

    parse_sentence(sentence, main_list)

main('grammer.txt', 'Bob saw a dog in the park')
