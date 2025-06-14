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