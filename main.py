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
        elif opcion == 'b':
            clave_img = input("Clave de la imagen médica cargada: ")
            if clave_img in dic_imagenes:
                img_medica = dic_imagenes[clave_img]
                ds = img_medica.get_dataset_list()[0]
                nombre = ds.PatientName if 'PatientName' in ds else "Anonimo"
                edad = ds.PatientAge if 'PatientAge' in ds else "Desconocida"
                ID = ds.PatientID if 'PatientID' in ds else "Sin ID"
                paciente = Paciente(nombre, edad, ID, img_medica.get_volumen())
                clave_pac = input("Clave para guardar el paciente: ")
                dic_pacientes[clave_pac] = paciente
                print(f"Paciente guardado con clave: {clave_pac}")
            else:
                print("Clave no encontrada.")
                