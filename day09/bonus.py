# Confirmar la fortaleza de un password
# Se van a ver también diccionarios. Su tipo de dato es dict.
# Ver con dir(dict) todos los métodos disponibles
# Consta de keys (serían como metadata) y values (los valores asociados a las keys)
password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
        break

result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
        break

result["upper-case"] = uppercase

print(result)

# La función all() aplicada a una lista/diccionario devuelve True si todos los elementos de la lista son True. En caso
# contrario devuelve False.
# Para una lista valdría all(result)
# Para diccionario, aplicarlo a las keys sería all(result.keys()). Para los valores sería all(result.values())
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
