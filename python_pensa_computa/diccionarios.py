"""my_dict = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50,
}

#acceder a un valor con llave
my_dict['David']

#si queremos evitar un error y nos de 30 si es q' no existe la llave 'Juan'
my_dict.get('Juan', 30)

my_dict.get('David', 30)

#Asignando a la llave Jaime un nuevo valor
my_dict['Jaime'] = 20 

#adicionar una llave y valor
my_dict['Pedro'] = 70

#borrar una llave
del my_dict['Jaime']

#iterando llaves
for llaves in my_dict.keys():

"values" para los valores

"items" para ambos tanto llaves y valores"""

#Dictionary compeehension
#modelo para las compeehensons en diccionarios
dict_variable = {key:value for (key,value) in dictonary.items()}


#usos 

numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)

#con compeheision reducimos código

new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)


------------------------------------------------------------

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)

----------------------------------------------------------------------------

# Initialize the `fahrenheit` dictionary 
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)