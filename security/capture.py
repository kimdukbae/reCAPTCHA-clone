from PIL import ImageGrab

img1 = ImageGrab.grab((17, 88, 196, 256))
saves = '{}'.format('1.jpg')
img1.save(saves)

img2 = ImageGrab.grab((217, 88, 396, 256))
saves = '{}'.format('2.jpg')
img2.save(saves)

img3 = ImageGrab.grab((417, 88, 596, 256))
saves = '{}'.format('3.jpg')
img3.save(saves)

img4 = ImageGrab.grab((17, 288, 196, 456))
saves = '{}'.format('4.jpg')
img4.save(saves)

img5 = ImageGrab.grab((217, 288, 396, 456))
saves = '{}'.format('5.jpg')
img5.save(saves)

img6 = ImageGrab.grab((417, 288, 596, 456))
saves = '{}'.format('6.jpg')
img6.save(saves)

img7 = ImageGrab.grab((17, 488, 196, 656))
saves = '{}'.format('7.jpg')
img7.save(saves)

img8 = ImageGrab.grab((217, 488, 396, 656))
saves = '{}'.format('8.jpg')
img8.save(saves)

img9 = ImageGrab.grab((417, 488, 596, 656))
saves = '{}'.format('9.jpg')
img9.save(saves)