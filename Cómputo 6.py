import face_recognition as fr
import os
import cv2 as cv
from time import sleep
import numpy as np

def get_encoded_faces():

    """"
    looks through the faces folder and encodes all the faces

    :return: dict of (name, image encoded)

    """"

    encoded = {}
    for dirpath, dnames, fnames in os.walk("./faces"):
            for f in fnames:
                  if f.endswith(".png") or f.endswith(".jpg"):
                        face = fr.load_image_file("faces/"  + f)
                        encoding = fr.face_encodings(face)[0]
                        encoded[ f.split(".")[0]] = encoding
    return encoded