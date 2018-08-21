from PIL import Image
import argparse as ap
from os import walk

imagePath = '../images/big/'
rotatedImgPath = '../images/rotated/'
resizedImgPath = '../images/resized/'
grayImagePath =  '../images/grayscale/'

def main():
    parser = ap.ArgumentParser(description = "Image Operation")
    parser.add_argument ("--resize", help="resize the image", type=str)
    parser.add_argument ("--rotate", help="rotate the image", type=int)
    parser.add_argument ("--grayscale", help="grayscale of the image", type=str)
    
    args, leftovers = parser.parse_known_args()

    if args.resize is not None:
        print("resize has been set (value is %s)" % args.resize)
        dimension = str(args.resize)
        resizeImage(dimension)
    
    if args.rotate is not None:
        degrees = int(args.rotate)
        print("rotate has been set (value is %s)" % args.rotate)
        rotateImage(imagePath,degrees)

    if args.grayscale is not None:
        print("grayscale has been set  to %s" % args.grayscale)
        if args.grayscale == "True":
            rgb2gray()
        else:
            print('images not set to grayscale')


def resizeImage(dimension):
    dimension = dimension.split("x")
    width = int(dimension[0])
    height = int(dimension[1])
    for  (dirpath, dirnames, filenames) in walk(imagePath):
        # print(filenames)
        for file in filenames:
            img = Image.open(imagePath + file)
            img = img.resize((width,height), Image.ANTIALIAS)
            img.save(resizedImgPath + file)

def rotateImage(path,degrees):
    for  (dirpath, dirnames, filenames) in walk(imagePath):
        # print(filenames)
        for file in filenames:
            img = Image.open(imagePath + file)
            img = img.rotate(degrees) 
            img.save(rotatedImgPath + file)

def rgb2gray():
    for  (dirpath, dirnames, filenames) in walk(imagePath):
        for file in filenames:
            img = Image.open(imagePath + file)
            img = img.convert('LA').convert('RGB') 
            img.save(grayImagePath + file)        

if __name__ == "__main__":
    main()
