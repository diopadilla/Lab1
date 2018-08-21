from PIL import Image
import argparse as ap
from os import walk
import matplotlib.pyplot as plt
import numpy as np


imagePath = '../images/big/'
file = 'img_12.jpg'

def main():
    parser = ap.ArgumentParser(description = "Image Operation")
    parser.add_argument ("--resize", help="resize image", type=str)
    parser.add_argument ("--rotate", help="rotate image", type=int)
    parser.add_argument("--grayscale", help= "displays grayscale of the image", type=str)
    args, leftovers = parser.parse_known_args()
    
    fig = plt.figure(figsize=(50,50)) #.subplots(nrows=1, ncols=3)
    

    if args.resize is not None:
        print("resize has been set (value is %s)" % args.resize)
        dimension = str(args.resize)
        img = resizeImage(dimension)
        fig.add_subplot(1,3,1)
        plt.imshow(img)

    if args.rotate is not None:
        degrees = int(args.rotate)
        print("rotate has been set (value is %s)" % args.rotate)
        img = rotateImage(degrees)
        fig.add_subplot(1,3,2)
        plt.imshow(img)
    if args.grayscale is not None:
        print("grayscale has been set  to %s" % args.grayscale)
        if args.grayscale == "True":
            img = rgb2gray()
            fig.add_subplot(1,3,3)
            plt.imshow(img)
        else:
            print('images not set to grayscale')
    plt.show(block=True) 

def rgb2gray():
    # Y' = 0.299 R + 0.587 G + 0.114 B
    img = Image.open(imagePath + file)
    # return np.dot(img[...,:3], [0.299, 0.587, 0.114])
    return img.convert('LA').convert('RGB')

def resizeImage(dimension):
    dimension = dimension.split("x")
    width = int(dimension[0])
    height = int(dimension[1])
    img = Image.open(imagePath + file)
    img = img.resize((width,height), Image.ANTIALIAS)
    return img
    
      

def rotateImage(degrees):
    img = Image.open(imagePath + file)
    # img.show()
    img = img.rotate(degrees) 
    # img.show()
    return img

if __name__ == "__main__":
    main()
