import cv2

def decodeQR(path):
    image = cv2.imread(path)
    detector = cv2.QRCodeDetector()
    data,points,_ = detector.detectAndDecode(image)
    return data