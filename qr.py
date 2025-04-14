import qrcode

qr = qrcode.QRCode(box_size=5, border=4)
qr.add_data("Hello World")
qr.make(fit=True)
img = qr.make_image(fill_color="limegreen", back_color="white")

img.save("qr-img.jpg")
