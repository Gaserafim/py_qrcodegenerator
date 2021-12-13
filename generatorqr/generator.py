import qrcode
import os

link = input('Digite ou cole o link a ser convertido para QR code:')
name_file = input('Dê um nome ao seu arquivo:')
generate_image = qrcode.make(link)
generate_image.save(os.path.join('image.png', os.path.expanduser(f'~/Desktop/{name_file}.png')))