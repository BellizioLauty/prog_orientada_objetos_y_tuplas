
#invertir el orden de una cadena
def invertir_cadena(cadena):
    invertida = ""
    for char in cadena:
        invertida = char + invertida
    return invertida

#contar palabras en una cadena
def contar_palabras(cadena):
    contador = 1 if cadena else 0
    for char in cadena:
        if char == " ":
            contador += 1
    return contador

#reemplazar una palabra en una cadena
def reemplazar_palabra(cadena, palabra_original, nueva_palabra):
    resultado = ""
    i = 0
    while i < len(cadena):
        if cadena[i:i+len(palabra_original)] == palabra_original:
            resultado += nueva_palabra
            i += len(palabra_original)
        else:
            resultado += cadena[i]
            i += 1
    return resultado

#convertir lista de peliculas en una cadena
def lista_peliculas_a_cadena(lista_peli):
    resultado = "Se recomienda ver "
    for sublista in lista_peli:
        for pelicula in sublista:
            resultado += f'"{pelicula}", '
    return resultado.rstrip(", ")

#capitalizar palabra en una cadena
def capitalizar_palabras(cadena):
    capitalizada = ""
    nueva_palabra = True
    for char in cadena:
        if nueva_palabra and "a" <= char <= "z":
            capitalizada += chr(ord(char) - 32)  # Convierte a mayúscula
            nueva_palabra = False
        else:
            capitalizada += char
        if char == " ":
            nueva_palabra = True
    return capitalizada

#verificar si una cadena es palindromo
def es_palindromo(cadena):
    cadena_sin_espacios = "".join([char for char in cadena if char != " "])
    return cadena_sin_espacios == invertir_cadena(cadena_sin_espacios)

#ordenar cadena ascendete o descendente
def ordenar_cadena(cadena, orden):
    # Convertimos la cadena en una lista de caracteres para ordenar
    caracteres = [char for char in cadena]
    # Ordenamiento simple usando burbuja, ya que no se permite el uso de sort
    for i in range(len(caracteres)):
        for j in range(0, len(caracteres) - i - 1):
            if (orden == 1 and caracteres[j] > caracteres[j + 1]) or (orden == -1 and caracteres[j] < caracteres[j + 1]):
                caracteres[j], caracteres[j + 1] = caracteres[j + 1], caracteres[j]
    return "".join(caracteres)