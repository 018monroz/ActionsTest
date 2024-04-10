import json

# Cargar el JSON existente desde un archivo o de alguna otra fuente
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)

v1 = datos['page']
v2 = datos['data'][0]['name']

print(v1)
print(v2)   
