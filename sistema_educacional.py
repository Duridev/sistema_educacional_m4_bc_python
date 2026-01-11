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
    