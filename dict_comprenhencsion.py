from math import sqrt

def run():
    my_dict = {i:i**3 for i in range(1, 11) if i % 3 != 0}

    print(my_dict)

    challen = {i: round(sqrt(i), 2) for i in range(1, 11)}

    print(challen)


if __name__ == '__main__':
    run()