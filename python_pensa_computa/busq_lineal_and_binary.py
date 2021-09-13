from random import randint
import time

def linear_search(values, target):
    for i in values:
        if i == target:
            return True
    return False


def binary_search(firts, end, values, target):
    if firts > end:
        return False

    half = (end + firts) // 2

    if target == values[half]:
        return True
    elif target < values[half]:
        return binary_search(firts, end - 1, values, target)
    else:
        return binary_search(firts + 1, end, values, target)

def run():
    print('Hello, welcome to the search engine...')
    values = int(input('\nWhat size will your list be?:  '))
    target = int(input('\nWhat number do you want to find?:  '))
    
    lis = [randint(0, 100) for i in range(values)]
    lis.sort() #ordenando de forma creciente
    option = input('\nWhat type of search do you want to use? (press 1 for linear or 2 for binary):  ')
    
    if option == '1':
        start = time.time_ns()
        search = linear_search(lis, target)
        end = time.time_ns()
    elif option == '2':
        start = time.time_ns()
        search = binary_search(0, len(lis), lis, target)
        end = time.time_ns()
    else:
        print('Only the given options are accepted...###')

    if search:
        print(f'Good, {target} is on the list... \n {lis}')
        print()
        print(f'En un tiempo de ejución de {end - start}.')
    else:
        print(f'Sad, {target} is not on the list... \n {lis}')



if __name__ == '__main__':
    run()