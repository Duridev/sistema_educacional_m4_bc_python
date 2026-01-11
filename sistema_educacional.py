class Asignatura:
    def __init__(self, nombre_asignatura, horas_semanales, numero_evaluaciones):
        self._nombre_asignatura = nombre_asignatura
        self._horas_semanales = horas_semanales
        self._numero_evaluaciones = numero_evaluaciones
        self._unidades = []
        self._fecha_pruebas = {}
        
    def agregar_unidad(self, nueva_unidad):
        self._unidades.append(nueva_unidad)
        
    def agregar_fecha_prueba(self, nueva_prueba, nueva_fecha):
        self._fecha_pruebas[nueva_prueba] = nueva_fecha
        
    def mostrar_unidades(self):
        print(f"La asignatura {self._nombre_asignatura} contiene las siguientes unidades: {self._unidades}")
        
    def programar_prueba(self):
        print(f"La programación de las pruebas es: {self._fecha_pruebas}")
    
    
class Alumno:
    def __init__(self, nombre, edad, rut, asignatura):
        self._nombre = nombre
        self._edad = edad
        self._rut = rut
        self._asignatura = asignatura
        
    def mostrar_datos(self):
        print(
            "*** Datos del alumno ***\n\n"
            f"Nombre: {self._nombre}"
            f"Edad: {self._edad}"
            f"Rut: {self._rut}"
              )
        
    def estudiar(self):
        print(f"El alumno {self._nombre} se ha puesto a estudiar")
        
    def tomar_asignatura(self):
        print(f"El alumno {self._nombre} a inscrito la asignatura {self._asignatura._nombre_asignatura}")
    
    def hacer_prueba(self):
        print(f"El alumno {self._nombre} a hecho la/s siguiente/s prueba/s: {self._asignatura._fecha_pruebas}")
    