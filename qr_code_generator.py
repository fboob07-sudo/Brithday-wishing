#url to QR code
#import qrcode as qr
#img = qr.make("https://fboob07-sudo.github.io/Brithday-wishing/")
#img.save("surprise.png")

#image to QR code
import qrcode

#Just a simple example of url to qr. to costomuize the QR you have to change the url.
img = qrcode.make("https://fboob07-sudo.github.io/Brithday-wishing/")
img.save("birthday_qr.png")
