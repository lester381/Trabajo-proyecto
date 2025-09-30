# defino los usuarios que pueden ingresar al correo
class mensaje:
    remitente: str
    destinatario: str
    asunto: str
    cuerpo: str

class user: 
    def __init__(self,email: str):
        self.email = email
        self.bandeja = []
        
class usuarios:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def existente(self,contraseña):
        return self.contraseña == contraseña
    
    def email(self):
        return self.email
    
    def recibir(self,msg: mensaje):
        self.append(msg)

    def listar(self):
        return list(self.bandeja)
    
class ServidorCorreo:
    def __init__(self):
        self.usuarios = {}
    
class funciones_usuario:
    def __init__(self):
        self.usuarios = []

    def inicio_sesion(self):
        nombre = input("Ingresa tu correo: ")
        contraseña = input("Ingresa tu contraseña: ")

        #busco en la base que el usuario coincida con su contraseña
        for u in self.usuarios:
            if u.nombre == nombre: 
                if u.contraseña == contraseña:
                    print("\nbienvenido al sistema de correos!\n")
                    return u
                else:
                    print("\nTu usuario o contraseña son incorrectos.\n")
                    return None
        print("\nTu usuario o contraseña son incorrectos.\n")
        return None
    
    def creacion_usuario(self):
        nombre = input("nombre de usuario: ")
        contraseña = input("ingresa tu contraseña: ")

        for u in self.usuarios:
            if u.nombre == nombre:
                print("\nusuario ya existente, porfavor, ingresa otro correo\n")
                return
        self.usuarios.append(usuarios(nombre,contraseña))
        print(f"\n{nombre} ingreso correctamente\n")
    
    def menu_principal(self):
        while True:
            print("¿Que desea hacer?")
            print("1) Iniciar sesion")
            print("2) Crear usuario")
            print("3) Listar usuarios")
            print("4) Registrar correo (Servidor)")
            print("5) Enviar mensaje (Servidor)")
            print("6) Ver bandeja (Servidor)")
            print("7) Salir\n")

            #condicion para elegir la opción del menu
            opcion = input("opcion: ")
            if opcion == "1": 
                self.inicio_sesion()
            elif opcion == "2":
                self.creacion_usuario()
            elif opcion == "3":
                self.listar_usuarios()
            elif opcion == "4":
                
            elif opcion == "5":
                
            elif opcion == "6":
                
            elif opcion == "7":
                break

men = funciones_usuario()
men.menu_principal()



