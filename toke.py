import json
import yaml

with open("myfile.json", 'r') as jason_file:
    ourjson = json.load(json_file)
print(ourjson)
print("su token de acceso es: {}".format(ourjson["acces_token"]))
print("su token de expiracion es: {} segunddo".format(oujson["expires_in"]))
