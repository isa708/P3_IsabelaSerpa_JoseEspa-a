from clases import Paciente, ImagenMedica, ImagenComun
import os
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
        
        if opcion == 'a':
            clave = input("Clave para guardar la imagen médica: ")
            carpeta = input("Ruta de la carpeta con DICOMs: ")
            img_medica = ImagenMedica(carpeta)
            img_medica.cargar_dicoms()
            img_medica.reconstruir_volumen()
            if img_medica.get_volumen() is not None:
                img_medica.mostrar_cortes()
            dic_imagenes[clave] = img_medica
            print(f"Imagen médica guardada con clave: {clave}")
            