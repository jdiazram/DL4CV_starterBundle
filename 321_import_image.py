#pip install opencv-contrib-python

import cv2

image = cv2.imread("images/example.png") #importar la imagen
print(image.shape) #imprimir dimensiones de la imagen
cv2.imshow("Image", image) #mostrar en ventana nueva
cv2.waitKey(0) #se espera para cerrar la ventana