import cv2

image = cv2.imread('image/image_01.jpg')

print(image.shape)  # tamanho da imagem em pixel da imagem 360x552 com 3 dimensões

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', image_gray)
print(image_gray.shape)  # tamanho da imagem em pixel da imagem 360x552 com 3 dimensões

cv2.waitKey()