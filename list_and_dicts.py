def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {"firstname": "Facundo", 'lastname':'García'}

    super_list = [
        {"firstname": "Facundo", 'lastname':'García'},
        {"firstname": "Miguel", 'lastname':'Torres'},
        {"firstname": "Cordova", 'lastname':'Poma'},
        {"firstname": "Jose", 'lastname':'Josue'},
        {"firstname": "Tabi", 'lastname':'Hernan'}
    ]
    
    super_dic = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, 0 -2, 25, 6],
        'floating_nums': [1.1, 4.5, .5, 6.43]
    }

    for key, value in super_dic.items():
        print(key, '-', value)
    
    print()

    for i in super_list:
        print(i['firstname'], i['lastname'])

if __name__ == '__main__':
    run()