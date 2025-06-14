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
        elif opcion == 'c':
            clave = input("Clave para guardar la imagen: ")
            ruta = input("Ruta de la imagen JPG/PNG: ")
            img_comun = ImagenComun(ruta)
            dic_imagenes[clave] = img_comun
            print(f"Imagen cargada con clave: {clave}")
            
        elif opcion == 'd':
            clave = input("Clave de la imagen médica: ")
            if clave in dic_imagenes and isinstance(dic_imagenes[clave], ImagenMedica):
                img_medica = dic_imagenes[clave]

                # Selección del corte
                indice = int(input("Índice del corte a trasladar (0 en adelante): "))

                # Menú fijo para dx
                print("\nSeleccione el valor para dx:")
                print("1. 50")
                print("2. 100")
                print("3. 150")
                print("4. 200")
                op_dx = int(input("Opción (1-4): "))
                if op_dx == 1:
                    dx = 50
                elif op_dx == 2:
                    dx = 100
                elif op_dx == 3:
                    dx = 150
                elif op_dx == 4:
                    dx = 200
                else:
                    print("Opción inválida. Se usará dx = 50.")
                    dx = 50
        # Menú fijo para dy
                print("\nSeleccione el valor para dy:")
                print("1. 50")
                print("2. 100")
                print("3. 150")
                print("4. 200")
                op_dy = int(input("Opción (1-4): "))
                if op_dy == 1:
                    dy = 50
                elif op_dy == 2:
                    dy = 100
                elif op_dy == 3:
                    dy = 150
                elif op_dy == 4:
                    dy = 200
                else:
                    print("Opción inválida. Se usará dy = 50.")
                    dy = 50

                # Aplicar traslación
                original, trasladada = img_medica.trasladar_imagen(indice, dx, dy)

                # Mostrar resultados
                from matplotlib import pyplot as plt
                fig, axs = plt.subplots(1, 2, figsize=(10, 5))
                axs[0].imshow(original, cmap='gray')
                axs[0].set_title("Original")
                axs[1].imshow(trasladada, cmap='gray')
                axs[1].set_title("Trasladada")
                plt.tight_layout()
                plt.show()