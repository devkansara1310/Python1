import pyqrcode
from pyqrcode import QRCode

s=input("Enter URL:")

url=pyqrcode.create(s)

url.svg("qrcode.svg",scale=8)
