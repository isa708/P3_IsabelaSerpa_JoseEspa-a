# Diccionarios para almacenar imágenes y pacientes
dic_pacientes = {}
dic_imagenes = {}

# Menú principal de operaciones
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("a) Procesar carpeta DICOM")
        print("b) Crear paciente desde DICOM cargado")
        print("c) Cargar imagen JPG o PNG")
        print("d) Trasladar imagen DICOM")
        print("e) Procesar imagen JPG/PNG")
        print("f) Salir")

        opcion = input("Seleccione una opción: ")
