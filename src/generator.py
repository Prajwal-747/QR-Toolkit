import qrcode

def generateQR(data, imgcolor="white", bgcolor="black"):
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
