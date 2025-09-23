# defino los usuarios que pueden ingresar al correo

usuarios = {
    "admin": "admin"
}

def inicio_sesion():
    print("inicio de sesion")
    usuario = input("Usuario:")
    contraseña = input("Contraseña:")
    if usuarios.get(usuario) == contraseña:
        print("\nUsuario registrado")
    else:
        print("\nUsuario no registrado\n")

#crea los usuarios que el usuario quiera
def creacion_de_usuario(): 
    print("Creción de usuario")
    usuario = input("Nombre de usuario:")
    contraseña = input("Ingresa la contraseña:")
    usuarios[usuario] = contraseña
    print("El usuario '{usuario}' se creo correctamente ")

#lista de usuarios disponibles para el uso
def listar_usuarios():
    print("Los correos cargados son:")
    for b in usuarios:
        print(b)
    
#muestreo del menu principal
def menu_principal():
    while True:
        print("¿Que desea hacer?")
        print("1) Iniciar sesion")
        print("2) Crear usuario")
        print("3) Listar usuarios\n")

        #condicion para elegir la opción del menu
        opcion = input("opcion:")
        if opcion == "1": 
            inicio_sesion()
        elif opcion == "2":
            creacion_de_usuario()
        elif opcion == "3":
            listar_usuarios()


menu_principal()



