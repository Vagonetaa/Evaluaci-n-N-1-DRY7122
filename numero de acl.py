
numero_acl = input("Ingrese el número de ACL IPv4: ")

if 1 <= int(numero_acl) <= 99:
    print("El número", numero_acl, "corresponde a una ACL Estándar.")
elif 100 <= int(numero_acl) <= 199:
    print("El número", numero_acl, "corresponde a una ACL Extendida.")
else:
    print("El número", numero_acl, "no corresponde a una lista de acceso.")
