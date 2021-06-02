"""
# Solución de tarea_49
# Autor: Juan Pablo Salado
# Fecha creación: 2021-06-01
# Fecha última modificación: 2021-06-02

# Tareas:
1.- Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes
    métodos para la clase:
    . Un constructor, donde los datos pueden estar vacíos.
    . Los setters y getters (métodos set y get) para cada uno de los atributos. Hay que validar las entradas de
    datos.
    . mostrar(): muestra los datos de la persona.
    . esMayorDeEdad(): devuelve un valor lógico indicando si es mayor de edad.

2.- Crea una clase llamada Cuenta que tendrá los siguientes atributos:
    . titular (que es una persona)
    . cantidad (puede tener decimales).
    El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
    . Un constructor, donde los datos pueden estar vacíos.
    . Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo
    ingresando o retirando dinero.
    . mostrar(): muestra los datos de la cuenta.
    . ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se
    hará nada.
    . retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""
import re


class Persona:
    __tabla_control_dni = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P',
                           9: 'D', 10: 'X', 11: 'B', 12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V',
                           18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'}

    def __init__(self, nombre: str = None, edad: int = None, dni: str = None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre: str):
        """ Fija el nombre validado de la instancia """
        try:
            # Forzar formato string
            nombre = str(nombre)
        except:
            raise ValueError()

        # Comprobar longitudes excesivas
        if len(nombre) > 50:
            raise ValueError("El nombre introducido es demasiado largo.")

        # Asignar nombre válido
        self.__nombre = nombre

    def get_nombre(self):
        """Devuelve el atributo nombre de la instancia """
        return self.__nombre

    def set_edad(self, edad: int):
        """ Fija la edad validada de la instancia """
        try:
            # Forzar formato entero
            edad = int(edad)
        except:
            raise ValueError

        # La edad ha de ser un valor mayor o igual a cero
        if edad < 0:
            raise ValueError("La edad ha de ser mayor o igual a 0.")

        # La edad ha de ser un valor mayor o igual a cero
        if edad >= 150:
            raise ValueError("La edad ha de ser menor que 150.")

        # Asignar edad válida
        self.__edad = edad

    def get_edad(self):
        """Devuelve el atributo edad de la instancia"""
        return self.__edad

    def set_dni(self, dni: str):
        """Fija el DNI validado de la instancia"""
        # Forzar formato string
        try:
            dni = str(dni)
        except:
            raise ValueError

        # Comprobar longitud y forma del DNI
        if not re.match('^[0-9]{8}[A-Za-z]$', dni):
            raise ValueError("Formato de DNI no válido.")

        # Comprobar si se trata de un DNI válido a través del dígito de control
        if self.__tabla_control_dni[int(dni[0:8]) % 23] != dni[-1].upper():
            raise ValueError("DNI no válido según carácter de control.")

        # Asignar DNI válido
        self.__dni = dni.upper()

    def get_dni(self):
        """Devuelve el atributo dni de la instancia"""
        return self.__dni

    def es_mayor_de_edad(self):
        """Determina si el objeto persona corresponde a un mayor de edad"""
        return True if self.__edad >= 18 else False

    def mostrar(self):
        print({'Nombre': self.get_nombre(), 'Edad': self.get_edad(), 'DNI': self.get_dni()})


def validar_cantidad(cantidad):
    """ Validad la cantidad a retirar o ingresar """
    # Forzar formato float
    try:
        cantidad = float(cantidad)
    except:
        raise ValueError

    # La cantidad ha de ser un valor mayor que cero
    if cantidad <= 0:
        raise ValueError("La cantidad ha de ser mayor de 0")

    return True


class Cuenta:
    def __init__(self, titular):
        self.__titular = titular
        self.__cantidad = 0.0

    def get_titular(self):
        """Devuelve el atributo titular de la clase instanciada"""
        return self.__titular

    def get_cantidad(self):
        """Devuelve el atributo cantidad de la clase instanciada"""
        return self.__cantidad

    def __set_titular(self, titular: str):
        """Fija el titular validado de la instancia"""
        # Forzar formato string
        try:
            titular = str(titular)
        except:
            raise ValueError()

        # Comprobar longitudes excesivas
        if len(titular) > 50:
            raise ValueError("El nombre introducido es demasiado largo.")

        # Asignar nombre válido
        self.__titular = titular

    def __set_cantidad(self, cantidad: float):
        """Fija la cantidad de la instancia"""
        self.__cantidad = cantidad

    def ingresar(self, cantidad):
        """ Añade una cantidad al atributo cuenta """
        if validar_cantidad(cantidad):
            self.__set_cantidad(self.__cantidad + cantidad)
            self.mostrar()

    def retirar(self, cantidad):
        """ Retira una cantidad del atributo cuenta """
        if not validar_cantidad(cantidad):
            return
        if self.__cantidad < cantidad:
            print("No hay suficientes fondos disponibles")
            return
        self.__set_cantidad(self.__cantidad - cantidad)
        self.mostrar()

    def mostrar(self):
        print({'Titular': self.get_titular(), 'Cantidad': self.get_cantidad()})


if __name__ == "__main__":
    pass
