import requests
import json

url = "https://reqres.in/api/user/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:

    print(response.text)
    # Carga los datos JSON en un diccionario
    data = response.json()

    # Especifica la ruta y el nombre del archivo JSON donde deseas guardar los datos
    archivo_json = 'datos.json'
    
    # Abre el archivo JSON en modo de escritura
    with open(archivo_json, 'w') as archivo:
        # Escribe los datos en el archivo JSON
        json.dump(data, archivo)
    print("Los datos han sido guardados correctamente en", archivo_json)
else:
    print("Error al realizar la solicitud a la API:", response.status_code)

print(response.text)
