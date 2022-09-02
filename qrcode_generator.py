import qrcode

url = input('Please enter the website link: ')
qrcode_name = input('Please enter the name of QR Code: ')

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='blue',back_color='white')
    img.save(f'{qrcode_name}.png')

generate_qrcode(url)