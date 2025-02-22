# Clase Estudiante
class Estudiante:
    # Constructor de la clase Estudiante
    def __init__(self, nombre, edad, calificacion):
        # Atributos de la clase
        self.nombre = nombre  # Asigna el nombre del estudiante
        self.edad = edad  # Asigna la edad del estudiante
        self.calificacion = calificacion  # Asigna la calificación del estudiante

    # Método para mostrar la información del estudiante
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")  # Muestra el nombre del estudiante
        print(f"Edad: {self.edad} años")  # Muestra la edad del estudiante
        print(f"Calificación: {self.calificacion}")  # Muestra la calificación del estudiante
        print()  # Imprime una línea en blanco para separar la información

# Crear objetos (instancias) de la clase Estudiante
estudiante1 = Estudiante("Margarito", 30, 85)  # Crea el primer estudiante
estudiante2 = Estudiante("Marcos", 28, 78)  # Crea el segundo estudiante

# Mostrar información de los estudiantes
print("Objeto 1")  # Imprime un título para el primer estudiante
estudiante1.mostrar_informacion()  # Llama al método para mostrar la información del primer estudiante
print("Objeto 2")  # Imprime un título para el segundo estudiante
estudiante2.mostrar_informacion()  # Llama al método para mostrar la información del segundo estudiante