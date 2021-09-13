def run():
    print("Ingrese palabra palindromo: ")

    palindrome = lambda string: string == string[::-1]

    print(palindrome(input()))


if __name__=='__main__':
    run()