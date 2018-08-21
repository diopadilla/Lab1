from PIL import Image
path = 'images/big/img_12.jpg'
width = 300

def resizeImage(path, width):
   
    img = Image.open(path)
    img.show()
    wpercent = (width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width,hsize))#, Image.ANTIALIAS)
    img.show()
    #img.save('sompic.jpg')

def rotateImage(path,degrees):
    

    basewidth = 300
    img = Image.open(path)
    img.show()
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.show()
    #img.save('sompic.jpg')

resizeImage(path, width)