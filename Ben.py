

# S > NP VP
# VP > V NP PP , VP PP
# PP > P NP
# V > "saw" , "ate" , "walked"
# NP > "John" , "Mary" , "Bob" , Det N PP , Det N
# Det > "a" , "an" , "the" , "my"
# N > "man" , "dog" , "cat" , "telescope" , "park"
# P > "in" , "on" , "by" , "with"

def open_grammer(filename):
    with open(filename) as file:
        text = file.readlines()
        for line in text:
            line.split('>')

open_grammer('grammer.txt')