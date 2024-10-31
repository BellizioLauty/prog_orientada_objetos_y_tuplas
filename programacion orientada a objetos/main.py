from prim_part import *

from segun_part import *

def main():
    # Ejemplo de la clase Libro
    print("Ejemplo de la clase Libro:")
    libro = Libro("Cien Años", "Gabriel García", 1990)
    print(libro.obtener_informacion())
    print()
    
    # Ejemplo de la clase Rectangulo
    print("Ejemplo de la clase Rectangulo:")
    rectangulo = Rectangulo(5, 10)
    print("Área:", rectangulo.calcular_area())
    print("Perímetro:", rectangulo.calcular_perimetro())
    print()
    
    # Ejemplo de la clase Calculadora
    print("Ejemplo de la clase Calculadora:")
    calculadora = Calculadora()
    print("Suma:", calculadora.sumar(5, 3))
    print("Resta:", calculadora.restar(5, 3))
    print("Multiplicación:", calculadora.multiplicar(5, 3))
    print("División:", calculadora.dividir(5, 3))
    print("División por cero:", calculadora.dividir(5, 0))
    print()
    
    # Ejemplo de las clases Animal, Perro, y Gato
    print("Ejemplo de las clases Animal, Perro, y Gato:")
    perro = Perro("Fido")
    gato = Gato("Michi")
    print(f"{perro.nombre} dice:", perro.hacer_sonido())
    print(f"{gato.nombre} dice:", gato.hacer_sonido())
    print()
    
    # Ejemplo de la clase CuentaBancaria
    print("Ejemplo de la clase CuentaBancaria:")
    cuenta = CuentaBancaria("Juan", 1000)
    print("Saldo inicial:", cuenta.obtener_saldo())
    print(cuenta.depositar(500))
    print("Saldo después de depósito:", cuenta.obtener_saldo())
    print(cuenta.retirar(300))
    print("Saldo después de retiro:", cuenta.obtener_saldo())
    print(cuenta.retirar(2000))
    print()
    

    # Ejemplo de invertir cadena
    print("Ejemplo de invertir cadena:")
    print(invertir_cadena("Hola mundo"))
    print()
    
    # Ejemplo de contar palabras
    print("Ejemplo de contar palabras:")
    print(contar_palabras("Hola mundo esto es una prueba"))
    print()
    
    # Ejemplo de reemplazar palabra
    print("Ejemplo de reemplazar palabra:")
    print(reemplazar_palabra("Hola mundo", "mundo", "universo"))
    print()
    
    # Ejemplo de convertir lista de películas en una cadena
    print("Ejemplo de convertir lista de películas en una cadena:")
    lista_peli = [
        ["Matrix", "El Padrino", "Titanic"],
        ["Forrest Gump", "Pulp Fiction", "Gladiador"]
    ]
    print(lista_peliculas_a_cadena(lista_peli))
    print()
    
    # Ejemplo de capitalizar palabras
    print("Ejemplo de capitalizar palabras:")
    print(capitalizar_palabras("hola mundo esto es una prueba"))
    print()
    
    # Ejemplo de verificar si es palíndromo
    print("Ejemplo de verificar si es palíndromo:")
    print(es_palindromo("anilina"))
    print(es_palindromo("hola"))
    print()
    
    # Ejemplo de ordenar cadena
    print("Ejemplo de ordenar cadena:")
    print(ordenar_cadena("dbca", 1))   # Ascendente
    print(ordenar_cadena("dbca", -1))  # Descendente
    print()

if __name__ == "__main__":
    main()