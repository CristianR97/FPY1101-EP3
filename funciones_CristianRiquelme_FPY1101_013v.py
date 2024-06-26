libros = []

def registrar_libros ():
    print()
    titulo = input("ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = input("Ingrese el año de publicacion: ")
    sku = input("ingrese el sku del libro: ")
    if titulo == ("Alas de hierro",{titulo}):
        int(input("Ingrese el autor:"))
        if autor == ("rebecca Yarros"):
            print ("Autor correcto")
        else:
            print ("Autor invalido")
            int(input("Ingrese año de publicacion: "))
            if año == 2024:
                print("Año correcto ")
            else:
                print("año incorrecto")
                int(input("Ingrese sku del libro: "))
                if sku == ("ALASDE-REB-2024"):
                    print ("Sku registrado con exito")
                else:
                    print("sku incorrecto")
    if titulo == ("La sombra de la sirena",{titulo}):
        int(input("ingrese el auto: "))
        if autor == ("camilla lackberg"):
            print ("Autor correcto")
        else:
            print("Autor invalido")
            int(input("Ingrese año de publicacion: "))
            if año == 2003:
                print("Año correcto ")
            else:
                print("Año incorrecto")
                int(input("Ingrese sku del libro: "))
            if sku == ("LASOMB-CAM-2003"):
                print("Sku registrado con exito")
            else:
                print("Sku incorrecto")


def prestar_libro ():
    print()
    int(input("Ingrese su usuario: "))
    int(input("Ingrese sku del libro: "))
    for sku in prestar_libro:
     if sku == ("ALASDE-REB-2024"):
        print("Este libro ya ha sido prestado a Cristian Riquelme.")
        if sku == ("LASOMB-CAM-2003"):
            print("Su prestamo se ha realizado con exito.")
        else:
            print("Opcion no valida.")


def listar_libros ():
    print()
    for titulo in listar_libros:
        print(f"{titulo['Alas de hierro']} {titulo['La sombra de la sirena']}")
        for autor in autor:
            print (f"{autor['Rebbeca Yarros']} {autor['Camilla Lackberg']} ")
            for sku in sku:
                print (f"{sku['ALASDE-REB-2024']} {sku['LASOMB-CAM-2003']}")
                for año in año:
                    print (f"{año[2024]} {año[2003]}")
            
def imprimir_reporte ():
    print()
    nombre_archivo = "imprimir_reporte.txt"
    with open (nombre_archivo, 'w') as file:
        for usuario in imprimir_reporte:
            file.write(f"{usuario['Cristian Riquelme']}{usuario['Juanin Juan Jarry']}")
            for titulo in imprimir_reporte:
                print (f"{titulo['Alas de hierro']} {titulo}['La sombra de la sirena']")
                for fecha in imprimir_reporte:
                    print (f"{fecha[15-5-2024]}{fecha[24-5-2024]}")


def salir_del_programa():
    print()    

def menu():
    while True:
            print ("* * * M E N Ú * * * ")
            op=int(input("1.Registrar libro\n2.Prestar libro\n3.Listar todos los libros\n4.Imprimir reporte de prestamos\n5.Salir del programa\nnOP: "))
            if op == 1:
                registrar_libros()
            elif op == 2:
                prestar_libro()
            elif op == 3:
                listar_libros()
            elif op == 4:
                imprimir_reporte()
            elif op == 5:
                print("saliendo del programa")
                break
            else:
                print("Opcion no valida. Intente nuevamente.")

def main():
    libros                
if __name__ == "__main__":
 main()             
