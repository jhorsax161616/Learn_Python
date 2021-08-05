def run():
    squares = [i**2 for i in range(1, 11) if i % 3 != 0]
    
    print(squares)

    challen = [i for i in range(1, 10000) if i % 4 == 0
                    and i % 6 == 0 and i % 9 == 0]
    
    print(challen)

if __name__ == '__main__':
    run()