import cv2 as cv2
import pytesseract


img = 'zdj1.jpeg'
img2 = 'zdj2.jpeg'
img3 = 'zdj3.jpg'
img4 = 'zdj4.jfif'
img5 = 'zdj5.jpg'
def convertImageToText(img):
    img = cv2.imread(img)
    print(pytesseract.image_to_string(img))

convertImageToText(img)
convertImageToText(img2)
convertImageToText(img3)
convertImageToText(img4)
convertImageToText(img5)

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'