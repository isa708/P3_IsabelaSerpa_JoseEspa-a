# Librerías necesarias
import pydicom
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

# Clase para almacenar datos de un paciente
class Paciente:
    def __init__(self, nombre, edad, ID, imagen):
        self.__nombre = nombre
        self.__edad = edad
        self.__ID = ID
        self.__imagen = imagen

    # Muestra información del paciente
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"ID: {self.__ID}")

    # Getters
    def get_nombre(self): return self.__nombre
    def get_edad(self): return self.__edad
    def get_ID(self): return self.__ID
    def get_imagen(self): return self.__imagen

    # Setters
    def set_nombre(self, nombre): self.__nombre = nombre
    def set_edad(self, edad): self.__edad = edad
    def set_ID(self, ID): self.__ID = ID
    def set_imagen(self, imagen): self.__imagen = imagen

    # Clase para gestionar imágenes médicas DICOM
class ImagenMedica:
    def __init__(self, carpeta):
        self.__carpeta = carpeta
        self.__dataset_list = []
        self.__volumen = None

    # Carga archivos DICOM de la carpeta
    def cargar_dicoms(self):
        archivos = sorted(os.listdir(self.__carpeta))
        for archivo in archivos:
            if archivo.endswith(".dcm"):
                ruta = os.path.join(self.__carpeta, archivo)
                ds = pydicom.dcmread(ruta)
                self.__dataset_list.append(ds)

    # Reconstruye un volumen 3D a partir de los DICOM cargados
    def reconstruir_volumen(self):
        self.__dataset_list.sort(key=lambda x: int(x.InstanceNumber))
        slices = [ds.pixel_array for ds in self.__dataset_list]
        self.__volumen = np.stack(slices, axis=0)

    # Muestra los tres cortes principales del volumen
    def mostrar_cortes(self):
        if self.__volumen is None:
            print("Primero debe reconstruir el volumen.")
            return

        transversal = self.__volumen[self.__volumen.shape[0] // 2, :, :]
        sagital = self.__volumen[:, :, self.__volumen.shape[2] // 2]
        coronal = self.__volumen[:, self.__volumen.shape[1] // 2, :]

        fig, axs = plt.subplots(1, 3, figsize=(15, 5))
        axs[0].imshow(transversal, cmap='gray')
        axs[0].set_title('Transversal')
        axs[1].imshow(sagital, cmap='gray', aspect='auto')
        axs[1].set_title('Sagital')
        axs[2].imshow(coronal, cmap='gray', aspect='auto')
        axs[2].set_title('Coronal')
        plt.tight_layout()
        plt.show()

    # Aplica traslación a una imagen DICOM seleccionada
    def trasladar_imagen(self, indice, dx, dy):
        original = self.__dataset_list[indice].pixel_array
        filas, columnas = original.shape
        M = np.float32([[1, 0, dx], [0, 1, dy]])
        trasladada = cv2.warpAffine(original, M, (columnas, filas))
        return original, trasladada

    # Getters
    def get_carpeta(self): return self.__carpeta
    def get_dataset_list(self): return self.__dataset_list
    def get_volumen(self): return self.__volumen

    # Setters
    def set_carpeta(self, carpeta): self.__carpeta = carpeta
    def set_volumen(self, volumen): self.__volumen = volumen