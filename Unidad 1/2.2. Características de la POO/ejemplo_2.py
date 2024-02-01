class Libro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - ISBN: {self.ISBN}"

    def prestamo(self):
        if self.disponible:
            print(f"El libro {self.titulo} ha sido prestado.")
            self.disponible = False
        else:
            print("El libro no está disponible para préstamo.")

    def devolucion(self):
        if not self.disponible:
            print(f"El libro {self.titulo} ha sido devuelto.")
            self.disponible = True
        else:
            print("El libro ya está disponible.")


class Usuario:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Usuario: {self.nombre} - Código: {self.codigo}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro {libro.titulo} añadido a la biblioteca.")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} añadido a la biblioteca.")

    def listar_libros(self):
        print("Lista de libros en la biblioteca:")
        for libro in self.libros:
            print(libro)

    def prestar_libro(self, libro, usuario):
        if libro in self.libros and usuario in self.usuarios:
            libro.prestamo()
        else:
            print("Libro o usuario no registrado en la biblioteca.")

    def devolver_libro(self, libro):
        if libro in self.libros:
            libro.devolucion()
        else:
            print("Libro no registrado en la biblioteca.")


# Ejemplo de uso del sistema de biblioteca

# Crear algunos libros y usuarios
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "978-84-450-7621-9")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-84-376-0494-7")
usuario1 = Usuario("Raul Ruidiaz", "001")
usuario2 = Usuario("Federica Miranda", "002")

# Crear la biblioteca
biblioteca = Biblioteca()

# Agregar libros y usuarios a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_usuario(usuario1)
biblioteca.agregar_usuario(usuario2)

# Listar libros en la biblioteca
biblioteca.listar_libros()

# Prestar y devolver libros
biblioteca.prestar_libro(libro1, usuario1)
biblioteca.prestar_libro(libro1, usuario2)  # Intentar prestar el mismo libro a otro usuario
biblioteca.devolver_libro(libro1)