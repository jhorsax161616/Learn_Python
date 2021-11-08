#Eliminando repetidos
def remove_duplicates(some_list):
    set_no_duplicate = set(some_list)
    some_list = list(set_no_duplicate)

    return some_list

def run():
    lista = [1, 1, 1, 2, 2, 2, 3, 3,4, 1]
    print(remove_duplicates(lista))

if __name__=='__main__':
    run()