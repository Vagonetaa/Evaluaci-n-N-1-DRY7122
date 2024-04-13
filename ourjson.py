import json

def abrir_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
            print(f"el archivo '{nombre_archivo}' no se encuentra")

if __name__=="_main_":
    ruta_archivo = "myfile.json"
    json_file = abrir_jason(ruta_archivo)

    if ourjson:
        print("contenido del archivo json:")
        print(ourjson)
