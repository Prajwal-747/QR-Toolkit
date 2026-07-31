import cv2

def decodeQR(path):
    """Decodes the QR from the given path

    Args:
        path (str): path of the image

    Returns:
        str: data from QR
    """
    image = cv2.imread(path)
    detector = cv2.QRCodeDetector()
    data,points,_ = detector.detectAndDecode(image)
    return data