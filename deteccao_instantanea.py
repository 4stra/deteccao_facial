from picamera import PiCamera
from time import sleep
import cv2

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/usuario/Desktop/image.jpg') #caminho para salvar a imagem
camera.stop_preview()
sleep(2)


imagem = cv2.imread("image.jpg") #caminho para a imagem
deteccao = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") #caminho para o algoritmo
imagemPB = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #conversao da imagem para preto e branco
face = deteccao.detectMultiScale(imagemPB, 1.3, 3)

for (x, y, largura, altura) in face:
    retangulo = cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 255, 0), 3)
    
cv2.imshow('', imagem)
cv2.waitKey(0)
