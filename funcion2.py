#Lucas Carabajal Division 1-A
# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
# un carácter como segundo y otro carácter  como tercero,  
# la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter 
# en la cadena

def reemplazarCaracteres(cadena:str,target:str,reemplazo:str)->str:
    lista_caracteres = list(cadena)
    contador = 0 
    for indice in range(len(lista_caracteres)):
        if lista_caracteres[indice] == target:
            lista_caracteres[indice] = reemplazo
            contador += 1 
            
    cadena = "".join(lista_caracteres)

    print(f"La cadena que paso se transformo en: {cadena}, y tuvo {contador} coincidencias ")
