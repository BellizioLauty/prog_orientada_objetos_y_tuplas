class Libro:
    def _init_(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def obtener_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}"

class Rectangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Calcula el área sin métodos adicionales
        return self.base * self.altura

    def calcular_perimetro(self):
        # Calcula el perímetro sin métodos adicionales
        return 2 * (self.base + self.altura)

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División entre cero no permitida"
        
class Animal:
    def _init_(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def hacer_sonido(self):
        return "guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "miau"
    
class CuentaBancaria:
    def _init_(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return "Depósito exitoso"
        else:
            return "Monto no válido"

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return "Retiro exitoso"
        else:
            return "Fondos insuficientes o monto no válido"

