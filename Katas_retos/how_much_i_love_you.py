from typing import Dict, List

def how_much_i_love_you(nb_petals) -> str:
    phrases : List = ["I love you", "a little", "a lot", "passionately", "madly",
    "not at all"]

    while nb_petals > len(phrases):
            nb_petals -= len(phrases)

    return phrases[nb_petals - 1]

#Optimo
def how_much_i_love_you2(nb_petals) -> str:
    phrases : List = ["I love you", "a little", "a lot", "passionately", "madly",
    "not at all"]

    return phrases[(nb_petals - 1) % 6]

if __name__=='__main__':
    print(how_much_i_love_you2(1))
    print(how_much_i_love_you2(2))
    print(how_much_i_love_you2(4))
    print(how_much_i_love_you2(6))
    print(how_much_i_love_you2(7))
    print(how_much_i_love_you2(15))
    print(how_much_i_love_you2(19))
