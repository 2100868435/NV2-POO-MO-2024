# Definición de la clase base
class Empleado:
    def __init__(self, nombre, edad, salario):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad  # Atributo encapsulado
        self._salario = salario  # Atributo encapsulado

    def descripcion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Salario: ${self._salario}"

    def calcular_bono(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase derivada Ingeniero
class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self._especialidad = especialidad

    def descripcion(self):
        return super().descripcion() + f", Especialidad: {self._especialidad}"

    def calcular_bono(self):
        return self._salario * 0.10

# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self._departamento = departamento

    def descripcion(self):
        return super().descripcion() + f", Departamento: {self._departamento}"

    def calcular_bono(self):
        return self._salario * 0.15

# Crear objetos de las clases
ingeniero1 = Ingeniero("Ana", 30, 70000, "Software")
gerente1 = Gerente("Luis", 45, 90000, "Ventas")

# Usar polimorfismo
empleados = [ingeniero1, gerente1]

for empleado in empleados:
    print(empleado.descripcion())
    print(f"Bono anual: ${empleado.calcular_bono()}")

