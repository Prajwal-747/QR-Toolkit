import qrcode

def generateQR(data, imgcolor="white", bgcolor="black"):
    """Generate QR code from given data

    Args:
        data (str): Text to URL to encode into the QR
        imgcolor (str, optional): foreground color of the QR Code. Defaults to "white".
        bgcolor (str, optional): Background Color of the QR Code. Defaults to "black".

    Returns:
        PIL.image.image: Generated QR code image
    """
    qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
    )

    qr.add_data(data=data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=imgcolor,back_color=bgcolor)
    return image